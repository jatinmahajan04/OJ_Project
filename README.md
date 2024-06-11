# Online Judge

### All project files added in branch master. Project information shown here:


## Overview

This project is an Online Judge system built using Django. It allows users to register, login, browse programming problems, submit solutions, and receive automated feedback on their submissions. The project consists of two main applications:
1. `accounts` - Handles user authentication and profile management.
2. `problems` - Manages problem statements, test cases, and submitted solutions.

## Features

- **User Authentication**: Registration, login, logout management.
- **Problem Management**: View programming problems.
- **Submission Management**: Submit solutions, view submission status, and results.
- **Automated Testing**: Automatic evaluation of submitted solutions against predefined test cases.

## Technologies Used

- **Django**: Web framework for the backend.
- **SQLite**: Default database for development (can be switched to PostgreSQL/MySQL for production).
- **HTML/CSS/JavaScript**: Frontend technologies for creating responsive and interactive UIs.
- **Bootstrap**: Frontend framework for styling.

## Applications

### Accounts

- **URLs**:
  - `/accounts/register/` - User registration.
  - `/accounts/login/` - User login.
  - `/accounts/logout/` - User logout.

- **Views**:
  - `RegisterView` - Handles user registration.
  - `LoginView` - Handles user login.
  - `LogoutView` - Handles user logout.

- **Models**:
  - `User` - The default Django user model.

### Problems

- **URLs**:
  - `/` - List all problems.
  - `/problem/<id>/` - GET: View problem details. POST: Submit solution to problem.
  - `/solution/<id>/` - View specific solution.
  - `leaderboard` - View specific solution.

- **Views**:
  - `ProblemListView` - Displays a list of all problems.
  - `SolutionResultView` - Displays the verdict for solution submitted.
  - `LeaderboardView` - Displays a list of ten recentmost solutions.
  - `ProblemDetailView` - Displays the details of a specific problem.

- **Models**:
  - `Problem` - Stores problem details including title, description, and difficulty.
  - `TestCase` - Stores test cases for each problem, including input and expected output.
  - `Solution` - Stores submitted solutions, including the user who submitted it, the problem it is for, the solution code, and the result of the automated testing.

