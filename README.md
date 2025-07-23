###🚀 Jenkins Waterfall Job Chain Setup
This documentation describes how to configure Jenkins freestyle jobs using post-build actions in a waterfall sequence: Dev → Test → Production.

⚙️ Step 1: Create Dev Job
<pre> ```bash # Jenkins Dashboard > New Item > "Dev" (Freestyle Project) # Git clone setup git clone https://github.com/your-username/jenkins-waterfall-model.git # Add Build Step → Execute Shell: python3 Dev.py > dev.txt # Post-build action: # → Build other projects: Test ``` </pre>
🧪 Step 2: Create Test Job
<pre> ```bash # Jenkins Dashboard > New Item > "Test" (Freestyle Project) # Git clone setup (same as Dev) git clone https://github.com/your-username/jenkins-waterfall-model.git # Build Step: python3 -m unittest test_Test.py > test.txt # Post-build action: # → Build other projects: Production ``` </pre>
🚀 Step 3: Create Production Job
<pre> ```bash # Jenkins Dashboard > New Item > "Production" (Freestyle Project) # Git clone setup git clone https://github.com/your-username/jenkins-waterfall-model.git # Build Step: python3 Production.py > production.txt ``` </pre>
▶️ Step 4: Trigger the Build Chain
<pre> ```bash # Go to "Dev" job in Jenkins and click: Build Now ``` </pre>
✅ This will auto-trigger:

Dev.py

→ Test.py + test_Test.py

→ Production.py

