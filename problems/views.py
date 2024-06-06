from django.shortcuts import render
from problems.models import Problem, Solution, Testcase
import subprocess
from pathlib import Path
from django.conf import settings
import uuid
from django.contrib.auth.decorators import login_required

# Create your views here.
@ login_required
def display_problem(request, prob_id):
    prob = Problem.objects.get(id=prob_id)
    context = { 
        "problem_id": prob_id,
        "problem_name": prob.name,
        "problem_statement": prob.statement,
        "problem_difficulty": prob.difficulty,
        'user': request.user
    }
    
    if request.method == 'GET':
        return render(request, "ind_problem.html", context)

    elif request.method == 'POST':
        code_solution = request.POST.get("solution")
        code_language = request.POST.get("language")
        verdict = evaluate_code(code_language,code_solution,prob_id)
        verdict = "Pass" if verdict else "Fail"
        print(request)
        sol = Solution.objects.create(language = code_language.capitalize(), code = code_solution, 
                                      author = request.user, problem = prob , verdict = verdict)
        
        context = {
            'solution': sol,
            'problem': prob,
            'user': request.user
        }
        display_solution(request, sol.id)
        return render(request, "solution_display.html", context)
        
@ login_required
def all_problems(request):
    if request.method == 'GET':
        all_prob = Problem.objects.all()

        context = {
            "problem_list": all_prob,
            'user': request.user
        }

        return render(request, "list_problem.html", context)


def evaluate_code(language, solution, problem_id):
    testcases = Testcase.objects.filter(problem = problem_id)
    for testcase in testcases:
        print(testcase.input, testcase.output)
        output = run_code(language, solution, testcase.input)
        if output.strip() != testcase.output.strip():
            return False
        print(output)
    return True


def run_code(language, code, input_data):
    project_path=Path(settings.BASE_DIR)    

    directories= ['codes','inputs', 'outputs']

    for directory in directories:
        directory_path = project_path / directory
        if not directory_path.exists():
            directory_path.mkdir(parents=True, exist_ok=True)
            
    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    with open(input_file_path, "w") as input_file:
        input_file.write(input_data)

    with open(output_file_path, "w") as output_file:
        pass  # This will create an empty file

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                    )
    elif language == "python":
        # Code for executing Python script
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["python3", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )

    # Read the output from the output file
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    return output_data

@ login_required
def leaderboard(request):
    if request.method == 'GET':
        top_ten_solutions = Solution.objects.all().order_by('-submitted_at')[:10]

        context = {
            "leaderboard": top_ten_solutions,
            'user': request.user
        }

        return render(request, "leaderboard.html", context)
    
@login_required 
def display_solution(request, solution_id):
    if request.method == 'GET':
        solution = Solution.objects.get(id=solution_id)
        problem = solution.problem
        user = request.user
        context =  {
            'solution': solution,
            'problem': problem,
            'user': user
        }
        return render(request, "solution_display.html", context)
