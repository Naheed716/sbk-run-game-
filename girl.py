import streamlit as st

st.set_page_config(page_title="SBK Physics Girl - Run From Exams!", page_icon="🏃‍♀️", layout="wide")

st.markdown("""
<style>
.main { background-color: #0f172a; }
h1 { color: white; text-align: center; }
p { color: #cbd5e1; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏃‍♀️ SBK Physics Girl - Run From Exams!</h1>", unsafe_allow_html=True)
st.markdown("<p><b>SBK Campus - Faculty of Basic Sciences is in FRONT. Run girl, run!</b> | EXAM is the BIGGEST zombie. Don't let them catch you!</p>", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { margin:0; background:#0f172a; font-family: Arial; overflow:hidden; }
  #gameWrap { width:100%; max-width:1000px; margin:auto; position:relative; }
  canvas { width:100%; height:520px; background:#87CEEB; border-radius:15px; border:4px solid white; display:block; }
  #ui { display:flex; justify-content:space-between; color:white; padding:10px; font-weight:bold; font-size:18px; }
  button { background:#ec4899; color:white; border:none; padding:12px 22px; border-radius:25px; font-size:16px; cursor:pointer; font-weight:bold; }
  button:hover { background:#db2777; }
  #controls { text-align:center; color:white; margin-top:8px; }
  .mobileBtn { background:#334155; color:white; border:2px solid white; padding:12px 18px; border-radius:12px; font-size:20px; margin:5px; }
</style>
</head>
<body>
<div id="gameWrap">
  <div id="ui">
    <div>❤️ Lives: <span id="lives">3</span> | 🏆 Score: <span id="score">0</span> | 📏 Distance: <span id="dist">0</span>m</div>
    <div><button onclick="startGame()">▶ START / RESTART</button></div>
  </div>
  <canvas id="game" width="1000" height="520"></canvas>
  <div id="controls">
    <p>⌨️ PC: SPACE / ↑ = Jump &nbsp; | &nbsp; → = Fast &nbsp; | &nbsp; ← = Slow &nbsp; | &nbsp; 📱 Mobile: Use Buttons Below</p>
    <button class="mobileBtn" onclick="jump()">⬆️ JUMP</button>
    <button class="mobileBtn" onclick="moveLeft()">⬅️</button>
    <button class="mobileBtn" onclick="moveRight()">➡️ FAST</button>
  </div>
</div>

<script>
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

let gameRunning = false, score=0, dist=0, lives=3, frame=0;
let girl = { x: 350, y: 340, w: 55, h: 95, vy: 0, jumping:false };
let zombies = [];
let clouds = [{x:100,y:60},{x:400,y:40},{x:700,y:70}];
let keys = {};

function startGame(){
  gameRunning=true; score=0; dist=0; lives=3; frame=0;
  girl={ x:350, y:340, w:55, h:95, vy:0, jumping:false };
  zombies=[
    { name:"EXAM", x:-150, y:330, w:95, h:130, speed:1.2, color:"#7f1d1d", emoji:"🧟" },
    { name:"QUIZ", x:-300, y:350, w:70, h:105, speed:1.6, color:"#14532d", emoji:"🧟" },
    { name:"PRESENTATION", x:-420, y:375, w:50, h:80, speed:2.0, color:"#581c87", emoji:"🧟" },
    { name:"ASSIGNMENT", x:-520, y:380, w:48, h:75, speed:2.2, color:"#1e3a8a", emoji:"🧟" },
  ];
  document.getElementById('lives').innerText=lives;
  document.getElementById('score').innerText=score;
  loop();
}

function jump(){ if(!girl.jumping){ girl.vy=-16; girl.jumping=true; } }
function moveLeft(){ girl.x=Math.max(200, girl.x-18); }
function moveRight(){ girl.x=Math.min(650, girl.x+18); }

document.addEventListener('keydown', e=>{
  keys[e.code]=true;
  if(e.code==='Space' || e.code==='ArrowUp'){ e.preventDefault(); jump(); }
});
document.addEventListener('keyup', e=>{ keys[e.code]=false; });

function drawBackground(){
  // Sky
  ctx.fillStyle="#87CEEB"; ctx.fillRect(0,0,1000,520);
  // Sun
  ctx.fillStyle="#fde047"; ctx.beginPath(); ctx.arc(850,70,45,0,Math.PI*2); ctx.fill();
  // Clouds
  ctx.fillStyle="white";
  clouds.forEach(c=>{ ctx.beginPath(); ctx.ellipse(c.x,c.y,55,22,0,0,Math.PI*2); ctx.fill(); ctx.beginPath(); ctx.ellipse(c.x+30,c.y+8,40,18,0,0,Math.PI*2); ctx.fill(); c.x+=0.4; if(c.x>1050) c.x=-100; });
  
  // FACULTY OF BASIC SCIENCES - In Front
  ctx.fillStyle="#fef3c7"; ctx.fillRect(620,110,360,240);
  ctx.fillStyle="#dc2626"; ctx.fillRect(620,110,360,35);
  ctx.fillStyle="white"; ctx.font="bold 18px Arial"; ctx.textAlign="center";
  ctx.fillText("FACULTY OF", 800, 132);
  ctx.fillText("BASIC SCIENCES", 800, 150);
  ctx.fillStyle="#1e293b"; ctx.font="bold 13px Arial"; ctx.fillText("SBK  •  PHYSICS DEPT", 800, 168);
  // Doors & Windows
  ctx.fillStyle="#0ea5e9"; ctx.fillRect(660,220,70,130); ctx.fillRect(760,220,70,130); ctx.fillRect(860,220,70,130);
  ctx.fillStyle="#78350f"; ctx.fillRect(770,280,60,70);
  ctx.fillStyle="#f59e0b"; ctx.font="bold 14px Arial"; ctx.fillText("🏃‍♀️ RUN TO SAFETY →", 800, 200);
  // Flag
  ctx.fillStyle="#166534"; ctx.fillRect(700,40,6,70); ctx.fillStyle="#22c55e"; ctx.fillRect(706,40,55,28);
  
  // Broad Campus Road
  ctx.fillStyle="#475569"; ctx.fillRect(0,380,1000,140);
  ctx.fillStyle="#f8fafc";
  for(let i=0;i<10;i++){ ctx.fillRect((i*120 + frame*2)%1100 -50, 445, 60, 8); }
  // Grass
  ctx.fillStyle="#22c55e"; ctx.fillRect(0,350,1000,30);
  // Trees
  ctx.fillStyle="#78350f"; ctx.fillRect(70,300,12,50); ctx.fillStyle="#16a34a"; ctx.beginPath(); ctx.arc(76,285,35,0,Math.PI*2); ctx.fill();
  ctx.fillStyle="#78350f"; ctx.fillRect(210,300,12,50); ctx.fillStyle="#16a34a"; ctx.beginPath(); ctx.arc(216,285,35,0,Math.PI*2); ctx.fill();
  ctx.fillStyle="white"; ctx.font="bold 16px Arial"; ctx.textAlign="left";
  ctx.fillText("SBK CAMPUS - BROAD ROAD", 20, 30);
}

function drawGirl(){
  let x=girl.x, y=girl.y;
  // Legs running
  ctx.fillStyle="#1e293b";
  let legMove = Math.sin(frame*0.4)*10;
  ctx.fillRect(x+12, y+65, 10, 30+legMove*0.3);
  ctx.fillRect(x+32, y+65, 10, 30-legMove*0.3);
  // Shoes
  ctx.fillStyle="#ec4899"; ctx.fillRect(x+8, y+92, 18, 8); ctx.fillRect(x+30, y+92, 18, 8);
  // Dress - Pink Physics Dress
  ctx.fillStyle="#f472b6"; ctx.beginPath(); ctx.moveTo(x+8, y+35); ctx.lineTo(x+48, y+35); ctx.lineTo(x+55, y+70); ctx.lineTo(x, y+70); ctx.closePath(); ctx.fill();
  ctx.fillStyle="white"; ctx.font="bold 11px Arial"; ctx.textAlign="center"; ctx.fillText("PHYSICS", x+28, y+58);
  // Arms
  ctx.fillStyle="#fcd7b0"; ctx.fillRect(x-5, y+38, 10, 25); ctx.fillRect(x+50, y+38, 10, 25);
  // Head - Pretty Girl
  ctx.fillStyle="#ffdab9"; ctx.beginPath(); ctx.arc(x+28, y+18, 24, 0, Math.PI*2); ctx.fill();
  // Hair - Long Black + Forehead Bangs
  ctx.fillStyle="#111827"; ctx.beginPath(); ctx.arc(x+28, y+12, 27, Math.PI, 0); ctx.fill();
  ctx.fillRect(x+2, y+2, 52, 30); // side hair
  // Bangs on forehead - pretty style
  ctx.fillStyle="#111827";
  for(let i=0;i<5;i++){ ctx.beginPath(); ctx.ellipse(x+10+i*9, y+5, 6, 9, 0, 0, Math.PI); ctx.fill(); }
  // Eyes - Big pretty eyes + lashes
  ctx.fillStyle="white"; ctx.beginPath(); ctx.arc(x+20, y+20, 5, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(x+36, y+20, 5, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle="black"; ctx.beginPath(); ctx.arc(x+21, y+21, 2.5, 0, Math.PI*2); ctx.fill(); ctx.beginPath(); ctx.arc(x+37, y+21, 2.5, 0, Math.PI*2); ctx.fill();
  // Blush + Smile
  ctx.fillStyle="#fda4af"; ctx.beginPath(); ctx.arc(x+15, y+28, 4, 0, Math.PI*2); ctx.fill(); ctx.beginPath(); ctx.arc(x+41, y+28, 4, 0, Math.PI*2); ctx.fill();
  ctx.strokeStyle="#be185d"; ctx.lineWidth=2; ctx.beginPath(); ctx.arc(x+28, y+26, 7, 0.2, Math.PI-0.2); ctx.stroke();
  // Backpack
  ctx.fillStyle="#8b5cf6"; ctx.fillRect(x+48, y+38, 12, 28);
  ctx.fillStyle="white"; ctx.font="bold 9px Arial"; ctx.fillText("SBK", x+54, y+55);
  // Scared label
  ctx.fillStyle="white"; ctx.font="bold 13px Arial"; ctx.fillText("😱 HELP!", x+28, y-18);
}

function drawZombies(){
  zombies.forEach(z=>{
    let x=z.x, y=z.y;
    // Body
    ctx.fillStyle=z.color; ctx.fillRect(x, y+35, z.w, z.h-35);
    // Head - Zombie green
    ctx.fillStyle="#84cc16"; ctx.beginPath(); ctx.arc(x+z.w/2, y+18, z.w/2.2, 0, Math.PI*2); ctx.fill();
    // Zombie eyes red
    ctx.fillStyle="red"; ctx.beginPath(); ctx.arc(x+z.w/3, y+15, 5, 0, Math.PI*2); ctx.fill(); ctx.beginPath(); ctx.arc(x+z.w*0.66, y+15, 5, 0, Math.PI*2); ctx.fill();
    // Mouth
    ctx.fillStyle="black"; ctx.fillRect(x+z.w/3, y+28, z.w/3, 6);
    // Arms forward - chasing
    ctx.fillStyle="#84cc16"; ctx.fillRect(x+z.w-5, y+40, 28, 10); ctx.fillRect(x+z.w-5, y+60, 28, 10);
    // Legs
    ctx.fillStyle="#1f2937"; ctx.fillRect(x+8, y+z.h-15, 12, 15); ctx.fillRect(x+z.w-20, y+z.h-15, 12, 15);
    // Name Label - BIG for EXAM
    ctx.fillStyle="white"; ctx.fillRect(x-5, y-28, z.w+10, 24);
    ctx.fillStyle=z.name==="EXAM" ? "red" : "black";
    ctx.font = z.name==="EXAM" ? "bold 16px Arial" : "bold 12px Arial";
    ctx.textAlign="center"; ctx.fillText(z.name, x+z.w/2, y-11);
    if(z.name==="EXAM") ctx.fillText("👹 BIGGEST", x+z.w/2, y-32);
  });
}

function loop(){
  if(!gameRunning) return;
  frame++;
  if(frame%10===0){ score+=1; dist+=1; document.getElementById('score').innerText=score; document.getElementById('dist').innerText=dist; }
  if(keys['ArrowRight']) girl.x=Math.min(650, girl.x+3);
  if(keys['ArrowLeft']) girl.x=Math.max(200, girl.x-2);

  // Gravity
  girl.vy+=0.8; girl.y+=girl.vy;
  if(girl.y>=340){ girl.y=340; girl.vy=0; girl.jumping=false; }

  // Zombies chase girl - speed increases
  zombies.forEach(z=>{
    z.x += z.speed + dist*0.005;
    // If zombie catches girl
    if(z.x+z.w > girl.x+5 && z.x < girl.x+girl.w-5 && Math.abs(z.y - girl.y) < 70){
      lives--; document.getElementById('lives').innerText=lives;
      z.x = -150 - Math.random()*300; // push back
      if(lives<=0){
        gameRunning=false;
        drawGameOver(z.name);
        return;
      }
    }
    // If zombie goes past, respawn behind
    if(z.x>1050) z.x=-100;
  });

  drawBackground();
  drawZombies();
  drawGirl();
  // Win check - reach faculty
  if(dist>150){
    ctx.fillStyle="rgba(0,0,0,0.7)"; ctx.fillRect(0,0,1000,520);
    ctx.fillStyle="#4ade80"; ctx.font="bold 45px Arial"; ctx.textAlign="center";
    ctx.fillText("🎉 YOU ESCAPED!", 500, 240);
    ctx.fillStyle="white"; ctx.font="bold 22px Arial";
    ctx.fillText("You reached Faculty of Basic Sciences!", 500, 285);
    ctx.fillText("Score: "+score, 500, 320);
    gameRunning=false; return;
  }
  requestAnimationFrame(loop);
}

function drawGameOver(killer){
  ctx.fillStyle="rgba(0,0,0,0.85)"; ctx.fillRect(0,0,1000,520);
  ctx.fillStyle="#ef4444"; ctx.font="bold 50px Arial"; ctx.textAlign="center";
  ctx.fillText("💀 GAME OVER 💀", 500, 210);
  ctx.fillStyle="white"; ctx.font="bold 24px Arial";
  ctx.fillText("The "+killer+" ZOMBIE caught you!", 500, 260);
  ctx.fillText("Physics Girl is DEAD... 😭", 500, 300);
  ctx.fillStyle="#fbbf24"; ctx.font="bold 20px Arial";
  ctx.fillText("Score: "+score+"  |  Distance: "+dist+"m", 500, 340);
  ctx.fillText("Press START to try again!", 500, 380);
}

drawBackground();
ctx.fillStyle="rgba(0,0,0,0.6)"; ctx.fillRect(0,0,1000,520);
ctx.fillStyle="white"; ctx.font="bold 35px Arial"; ctx.textAlign="center";
ctx.fillText("Press START to Run!", 500, 250);
ctx.font="bold 18px Arial"; ctx.fillText("Escape EXAM, QUIZ, PRESENTATION & ASSIGNMENT", 500, 285);
</script>
</body>
</html>
"""

st.components.v1.html(game_html, height=680, scrolling=False)

st.markdown("---")
st.markdown("**Made for SBK Physics Students 💖 | Share this link with your friends, they can't steal your code if repo is Private!**")
st.markdown("**Tip:** Agar game slow lage to `START` dabao, phir `➡️ FAST` se bhago aur `⬆️ JUMP` se bacho.")
</script>
