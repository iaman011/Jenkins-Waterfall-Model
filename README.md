### Jenkins Waterfall Job Chain Setup
This documentation describes how to configure Jenkins freestyle jobs using post-build actions in a waterfall sequence: Dev → Test → Production.

### ⚙️ Step 1: Create Dev Job
<pre>  # Jenkins Dashboard <br /> New Item <br /> "Dev" (Freestyle Project)<br /> # Git clone setup git clone https://github.com/your-username/jenkins-waterfall-model.git # Add Build Step <br /> Execute Shell: python Dev.py  <br /># Post-build action: <br /># Build other projects: Test  </pre>
### 🧪 Step 2: Create Test Job
<pre>  # Jenkins Dashboard > New Item > "Test" (Freestyle Project) # Git clone setup (same as Dev) git clone https://github.com/your-username/jenkins-waterfall-model.git<br /> # Build Step: Test.py <br /> test.txt <br /># Post-build action: <br /># → Build other projects: Production  </pre>
### 🚀 Step 3: Create Production Job
<pre>  # Jenkins Dashboard <br /> New Item <br /> "Production" (Freestyle Project)<br /> # Git clone setup git clone https://github.com/your-username/jenkins-waterfall-model.git<br /> # Build Step: python Production.py  </pre>
### ▶️ Step 4: Trigger the Build Chain
<pre>  # Go to "Dev" job in Jenkins and click: Build Now  </pre><br />
✅ This will auto-trigger:

Dev.py

→ Test.py + test_Test.py

→ Production.py

