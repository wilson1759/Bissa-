from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Docker - Mon Nom</title>
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0b0c10;
            color: #f5f5f7;
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(0,229,255,0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,229,255,0.04) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: 0;
        }
        .container {
            position: relative;
            z-index: 1;
            text-align: center;
            padding: 3rem 2rem;
            max-width: 680px;
            width: 100%;
        }
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(0,229,255,0.08);
            border: 1px solid rgba(0,229,255,0.25);
            border-radius: 999px;
            padding: 6px 20px;
            font-size: 0.75rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #00e5ff;
            margin-bottom: 2rem;
        }
        .dot {
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #00e5ff;
            animation: pulse 1.5s ease-in-out infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; } 50% { opacity: 0.3; }
        }
        h1 {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2rem, 5vw, 3.5rem);
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 1rem;
        }
        h1 span {
            background: linear-gradient(135deg, #00e5ff, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .subtitle {
            color: #6b6b80;
            font-size: 1rem;
            font-weight: 300;
            line-height: 1.7;
            margin-bottom: 2.5rem;
        }
        .cards {
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
        }
        .card {
            background: #12121a;
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 14px;
            padding: 1.2rem 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            text-align: left;
            transition: border-color 0.2s, transform 0.2s;
        }
        .card:hover {
            border-color: rgba(0,229,255,0.3);
            transform: translateY(-2px);
        }
        .card-icon { font-size: 1.4rem; flex-shrink: 0; }
        .card-label {
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #6b6b80;
            margin-bottom: 3px;
        }
        .card-value { font-size: 0.9rem; font-weight: 500; }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge"><div class="dot"></div>Application conteneurisée · Docker</div>
        <h1>Bonjour à tous !<br><span>Flask + Docker</span></h1>
        <p class="subtitle">Application web simple déployée avec Docker<br>dans le cadre du CC1 — KEYCE Informatique</p>
        <div class="cards">
            <div class="card">
                <div class="card-icon">🐳</div>
                <div>
                    <div class="card-label">Technologie</div>
                    <div class="card-value">Docker · Python 3.9 · Flask</div>
                </div>
            </div>
            <div class="card">
                <div class="card-icon">🌐</div>
                <div>
                    <div class="card-label">Port exposé</div>
                    <div class="card-value">0.0.0.0 : 5000</div>
                </div>
            </div>
            <div class="card">
                <div class="card-icon">👤</div>
                <div>
                    <div class="card-label">Développé par</div>
                    <div class="card-value">TON_NOM — CC1 Méthode Agile / DevOps 2026</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)