const canvas = document.getElementById("radarCanvas");
const ctx = canvas.getContext("2d");
const threatsP = document.getElementById("threats");

function drawRadar(threats) {
    ctx.clearRect(0, 0, 400, 400);
    ctx.strokeStyle = "red";
    ctx.beginPath();
    ctx.arc(200, 200, 180, 0, 2 * Math.PI);
    ctx.stroke();

    threats.forEach(threat => {
        const angle = (Math.PI / 180) * threat.direction;
        const r = (threat.distance / 1000) * 180;
        const x = 200 + r * Math.cos(angle);
        const y = 200 + r * Math.sin(angle);
        ctx.fillStyle = threat.type === "drone" ? "cyan" : "orange";
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, 2 * Math.PI);
        ctx.fill();
    });

    threatsP.innerHTML = threats.map(t => 
        `${t.type.toUpperCase()} – ${t.distance}m @ ${t.direction}°`
    ).join("<br>");
}

async function updateRadar() {
    const threats = await fetch("/api/radar").then(r => r.json());
    drawRadar(threats);
}

setInterval(updateRadar, 2000);
updateRadar();
