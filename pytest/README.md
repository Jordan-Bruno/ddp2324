# Instructions for Installing pytest

## Steps to Follow

1. **Open Visual Studio Code (VSCode).**

2. **Access the built-in terminal:**

   - Look at the top of the window to find the main menu.
   - Click on 'Terminal' in the menu bar.
   - In the drop-down menu that appears, select 'New Terminal'.

3. **In the terminal, first check if you have `pytest` installed by typing:**

   ```bash
   pytest --version
   ```

   - If you see a version number, `pytest` is already installed.
   - If you get an error or message saying 'pytest' is not recognised, proceed to the next step.

4. **To install pytest, use the pip command:**

   ```bash
   pip install pytest
   ```

   - On some systems, you might need to use `pip3` instead of `pip`.

5. **After installation, you can verify it by typing again in the terminal:**

   ```bash
   pytest --version
   ```

   - This should now show the installed version of `pytest`.

6. **If you encounter any issues during installation, ensure that Python and pip are correctly installed and added to your system's PATH.**

7. **Once pytest is installed, you can use it to run tests in your Python projects by following these steps:**

   - Open the terminal.
   - Ensure your current directory is the root of your Python project or the directory containing your test files.
   - In the terminal, type the command `python -m pytest <TestFileName>` and press Enter.
