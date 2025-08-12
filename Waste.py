<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Student Finance — MVP Playground</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
  <script src="https://kit.fontawesome.com/yourkitid.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.3.0/dist/chart.umd.min.js"></script>
  <style>
    /* [ SAME CSS FROM YOUR VERSION — unchanged ] */
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#97a0b7; --accent:#7c5cff; --accent-2:#24d29f; --glass: rgba(255,255,255,0.03);
      --glass-2: rgba(255,255,255,0.02); --glass-3: rgba(255,255,255,0.06);
      font-synthesis: none;
    }
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;background:linear-gradient(180deg,#071026 0%, #081225 50%, #04111b 100%);font-family:Inter,system-ui,Segoe UI,Roboto,'Helvetica Neue',Arial; color:#dce7ff}
    .app{max-width:1200px;margin:28px auto;padding:24px;display:grid;grid-template-columns:360px 1fr;gap:20px}
    header{display:flex;align-items:center;gap:16px}
    .brand{display:flex;align-items:center;gap:12px}
    .logo{width:56px;height:56px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#4f8bff);display:flex;align-items:center;justify-content:center;font-weight:800;font-family:Montserrat;color:white;box-shadow:0 6px 20px rgba(124,92,255,0.18)}
    .title{line-height:1}
    .title h1{margin:0;font-size:18px}
    .title p{margin:0;color:var(--muted);font-size:12px}
    .sidebar{background:linear-gradient(180deg,var(--card),#061124);border-radius:14px;padding:18px;box-shadow:0 8px 30px rgba(2,6,23,0.8);height:calc(100vh - 92px);overflow:auto}
    .profile{display:flex;gap:12px;align-items:center;margin-bottom:16px}
    .avatar{width:56px;height:56px;border-radius:10px;background:linear-gradient(180deg,#2d3966,#1b2340);display:flex;align-items:center;justify-content:center;font-weight:700}
    .muted{color:var(--muted);font-size:13px}
    .nav{margin-top:12px;display:flex;flex-direction:column;gap:8px}
    .nav button{display:flex;gap:12px;align-items:center;padding:10px;border-radius:10px;border:none;background:transparent;color:var(--muted);text-align:left;cursor:pointer}
    .nav button.active{background:linear-gradient(90deg,rgba(124,92,255,0.14),rgba(36,210,159,0.03));color:#fff}
    .main{min-height:80vh}
    .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:14px}
    .card{background:var(--glass);padding:14px;border-radius:12px;box-shadow:0 6px 20px rgba(2,6,23,0.6)}
    .big{grid-column:span 2}
    /* ... rest of your CSS remains unchanged ... */
  </style>
</head>
<body>
<div class="app">
  <div>
    <header>
      <div class="brand">
        <div class="logo">SF</div>
        <div class="title"><h1>StudentFinance</h1><p class="muted">MVP playground</p></div>
      </div>
    </header>
    <div class="sidebar">
      <div class="profile">
        <div class="avatar">N</div>
        <div>
          <div style="font-weight:700">Nakul</div>
          <div class="muted">Student • Demo account</div>
        </div>
      </div>
      <div class="nav">
        <button class="active" data-view="dashboard">Dashboard</button>
        <button data-view="expenses">Expenses</button>
        <button data-view="bills">Bill Split & Reminders</button>
        <button data-view="savings">Micro-Savings</button>
        <button data-view="chatbot">AI Tips</button>
        <button data-view="challenges">Challenges</button>
        <button data-view="settings">Settings</button>
      </div>
    </div>
  </div>

  <main class="main">
    <!-- DASHBOARD -->
    <section class="view" data-view="dashboard">
      <div class="grid">
        <!-- Financial Health Card -->
        <div class="card big">
          <div class="section-title"><h3>Financial Health</h3><div class="tiny">Updated live</div></div>
          <div style="display:flex;gap:18px;align-items:center">
            <div class="health-score">
              <div class="score" id="healthScore">--</div>
              <div>
                <div class="muted-sm">Overall Score</div>
                <div class="lead" id="scoreText">--</div>
                <div class="progress" style="margin-top:8px"><i id="progressBar"></i></div>
              </div>
            </div>
            <div style="flex:1">
              <div style="display:flex;gap:12px;"> 
                <div class="card" style="flex:1;padding:12px;"> <div class="tiny">Balance</div><div style="font-weight:700;font-size:20px" id="balance">₹0</div></div>
                <div class="card" style="flex:1;padding:12px;"> <div class="tiny">Monthly Spend</div><div style="font-weight:700;font-size:20px" id="monthlySpend">₹0</div></div>
                <div class="card" style="flex:1;padding:12px;"> <div class="tiny">Savings</div><div style="font-weight:700;font-size:20px" id="savingsTotal">₹0</div></div>
              </div>
              <div style="margin-top:10px" id="insights"> </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- EXPENSES -->
    <section class="view" data-view="expenses" style="display:none">
      <div class="card big">
        <div class="section-title"><h3>Expenses</h3><div class="muted-sm">Auto-categorize (demo)</div></div>
        <div style="display:flex;gap:8px;margin-bottom:8px">
          <input id="expenseTitle" placeholder="Title" />
          <select id="expenseCat">
            <option value="food">Food</option>
            <option value="transport">Transport</option>
            <option value="rent">Rent</option>
            <option value="entertainment">Entertainment</option>
            <option value="utilities">Utilities</option>
            <option value="others">Others</option>
          </select>
          <input id="expenseAmt" type="number" placeholder="₹0" />
          <button class="btn" id="addExpense">Add</button>
        </div>
        <div id="expensesList" class="list" style="max-height:320px;overflow:auto"></div>
      </div>
    </section>

    <!-- BILLS -->
    <section class="view" data-view="bills" style="display:none">
      <div class="card">
        <div class="section-title"><h3>Upcoming Bills</h3><div class="muted-sm"><button class="btn btn-ghost" id="detectRecurring">Detect Recurring</button></div></div>
        <div id="billsList" class="list"></div>
      </div>
      <div class="card">
        <div class="section-title"><h3>Bill Split — Roommates</h3></div>
        <div style="display:flex;gap:8px;margin-bottom:10px">
          <input id="roomName" placeholder="Roommate name" />
          <input id="roomShare" type="number" placeholder="Share %" />
          <button class="btn" id="addRoommate">Add</button>
        </div>
        <div id="roomList" class="list"></div>
        <div style="margin-top:10px;display:flex;gap:8px">
          <input id="billTitle" placeholder="Bill title" />
          <input id="billAmt" type="number" placeholder="₹0" />
          <button class="btn" id="splitBill">Split</button>
        </div>
      </div>
    </section>

    <!-- SAVINGS -->
    <section class="view" data-view="savings" style="display:none">
      <div class="card">
        <div class="section-title"><h3>Micro-savings Goals</h3></div>
        <div id="goalsList" class="list"></div>
        <div style="margin-top:10px;display:flex;gap:8px">
          <input id="goalName" placeholder="Goal name" />
          <input id="goalAmt" type="number" placeholder="Target ₹" />
          <button class="btn" id="addGoal">Add</button>
        </div>
        <div style="margin-top:12px" class="muted-sm">
          Round-up: <label><input type="checkbox" id="roundupToggle"/> Round up transactions</label>
        </div>
      </div>
    </section>

    <!-- CHATBOT -->
    <section class="view" data-view="chatbot" style="display:none">
      <div class="card">
        <div class="section-title"><h3>AI Budgeting Tips</h3></div>
        <div id="chatLog" style="height:160px;overflow:auto;padding:8px;background:var(--glass);border-radius:8px"></div>
        <div style="display:flex;gap:8px;margin-top:8px">
          <input id="chatMsg" placeholder="Ask for a tip" />
          <button class="btn" id="sendChat">Ask</button>
        </div>
      </div>
    </section>

    <!-- CHALLENGES -->
    <section class="view" data-view="challenges" style="display:none">
      <div class="card">
        <div class="section-title"><h3>Leaderboard</h3></div>
        <div id="leaderboard" class="leaderboard"></div>
        <div style="margin-top:8px;display:flex;gap:8px">
          <input id="challengeName" placeholder="Challenge name" />
          <button class="btn" id="startCh">Start</button>
        </div>
      </div>
    </section>

    <!-- SETTINGS -->
    <section class="view" data-view="settings" style="display:none">
      <div class="card">
        <h3>Settings</h3>
        <p>Settings panel coming soon...</p>
      </div>
    </section>
  </main>
</div>

<script>
/* All your JS logic is the same — just adding the view switching: */
document.querySelectorAll('.nav button').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.querySelectorAll('.nav button').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const view = btn.dataset.view;
    document.querySelectorAll('.view').forEach(sec=>{
      sec.style.display = (sec.dataset.view === view) ? '' : 'none';
    });
  });
});
</script>
<!-- Rest of your original JS from renderAll(), state handling, etc. here -->
</body>
</html>
