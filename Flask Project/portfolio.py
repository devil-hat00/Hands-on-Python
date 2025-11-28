from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tarun Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">

<style>
    body{
        margin:0;
        font-family:'Roboto',sans-serif;
        background:#121212;
        color:#e0e0e0;
    }

    a{text-decoration:none;color:inherit;}

    nav{
        display:flex;
        justify-content:space-between;
        padding:1rem 2rem;
        background:#1f1f1f;
        position:sticky;
        top:0;
        z-index:10;
    }

    .logo{font-size:1.6rem;font-weight:700;color:#00ff99;}

    .nav-links{
        list-style:none;
        display:flex;
        gap:1.8rem;
    }

    .nav-links li a:hover{color:#00ff99;}

    section{
        padding:4rem 2rem;
        max-width:900px;
        margin:auto;
    }

    h2{
        text-align:center;
        color:#00ff99;
        margin-bottom:2rem;
    }

    #home{
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        text-align:center;
        background:linear-gradient(135deg,#1f1f1f,#121212);
    }

    #home h1{font-size:3rem;}
    #home span{color:#00ff99;}

    .projects-container{
        display:flex;
        flex-wrap:wrap;
        justify-content:center;
        gap:2rem;
    }

    .project-card{
        background:#1f1f1f;
        padding:1.4rem;
        width:250px;
        border-radius:10px;
        transition:.25s;
    }

    .project-card:hover{
        transform:translateY(-7px);
        box-shadow:0 0 14px #00ff99;
    }

    .skills-container{
        display:flex;
        flex-wrap:wrap;
        justify-content:center;
        gap:1rem;
    }

    .skills-container span{
        background:#1f1f1f;
        padding:.7rem 1rem;
        border-radius:6px;
        transition:.25s;
    }

    .skills-container span:hover{
        background:#00ff99;
        color:#121212;
    }

    #achievements ul{
        max-width:700px;
        list-style:square;
        margin:auto;
    }

    form{
        display:flex;
        flex-direction:column;
        gap:1rem;
        max-width:450px;
        margin:auto;
    }

    input,textarea{
        background:#1f1f1f;
        border:none;
        padding:.8rem;
        color:#e0e0e0;
        border-radius:5px;
    }

    input:focus,textarea:focus{
        outline:2px solid #00ff99;
    }

    button{
        padding:.8rem;
        background:#00ff99;
        border:none;
        font-weight:700;
        border-radius:5px;
        cursor:pointer;
        color:#121212;
    }

    button:hover{background:#00cc7a;}

    footer{
        background:#1f1f1f;
        padding:2rem;
        text-align:center;
        margin-top:2rem;
    }

    @media(max-width:768px){
        .nav-links{flex-direction:column;gap:1rem;}
        .projects-container{flex-direction:column;}
    }
</style>
</head>

<body>

<nav>
    <div class="logo">TS</div>
    <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#skills">Skills</a></li>
        <li><a href="#achievements">Achievements</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</nav>

<section id="home">
    <div>
        <h1>Hello, I'm <span>Tarun Sharma</span></h1>
        <p>CEO & Engineer | Building smart systems in AI, Web, and Automation</p>
    </div>
</section>

<section id="about">
    <h2>About Me</h2>
    <p>I am an engineer and founder of Torque Zero. I build AI-driven tools, clean UI apps, and systems that solve actual real-world problems.</p>
</section>

<section id="projects">
    <h2>Projects</h2>

    <div class="projects-container">
        <div class="project-card">
            <h3>Sync Core</h3>
            <p>Offline-first communication system built for colleges using Python.</p>
        </div>

        <div class="project-card">
            <h3>Medura</h3>
            <p>AI-based community health & disease prediction platform.</p>
        </div>
    </div>
</section>

<section id="skills">
    <h2>Skills</h2>

    <div class="skills-container">
        <span>Python</span>
        <span>AI & ML</span>
        <span>IoT</span>
        <span>Web Dev</span>
        <span>Data Analysis</span>
    </div>
</section>

<section id="achievements">
    <h2>Achievements</h2>
    <ul>
        <li>Developed Medura for community health analysis</li>
        <li>Built Sync Core for institutional communication</li>
        <li>Speaker at AI & tech events</li>
    </ul>
</section>

<section id="contact">
    <h2>Contact Me</h2>

    <form>
        <input type="text" placeholder="Your Name" required>
        <input type="email" placeholder="Your Email" required>
        <textarea placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
</section>

<footer>
    <p>&copy; 2025 Boss. All rights reserved.</p>
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
