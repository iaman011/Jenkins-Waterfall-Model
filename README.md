### Step-by-Step Jenkins Configuration
🔧 Step 1: Create Dev Job
bash
Copy
Edit
# In Jenkins UI:
# Dashboard > New Item > Dev (Freestyle Project)

# Configure Git
git clone https://github.com/your-user/jenkins-waterfall-model.git

# Build Command
python3 Dev.py > dev.txt

# Post-build Action
# Build other projects: Test
🔧 Step 2: Create Test Job
bash
Copy
Edit
# Dashboard > New Item > Test (Freestyle Project)

# Configure Git (same repo)
git clone https://github.com/your-user/jenkins-waterfall-model.git

# Build Command
python3 -m unittest test_Test.py > test.txt

# Post-build Action
# Build other projects: Production
🔧 Step 3: Create Production Job
bash
Copy
Edit
# Dashboard > New Item > Production (Freestyle Project)

# Configure Git (same repo)
git clone https://github.com/your-user/jenkins-waterfall-model.git

# Build Command
python3 Production.py > production.txt
▶️ Step 4: Trigger the Build Chain
bash
Copy
Edit
# Go to Dev job in Jenkins and click:
Build Now
✅ This will automatically:

Run Dev.py

Then trigger Test

Then trigger Production

