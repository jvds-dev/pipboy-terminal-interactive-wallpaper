const pipboyElement = document.querySelector(".pipboy")

async function fetchStatus() {
    const res = await fetch("http://192.168.1.216:5000/sys");
    return res.json();
}

async function updateImage() {
    const theme = document.documentElement.dataset.theme;
    let data;
    try {
        data = await fetchStatus();
    } catch (err) {
        console.warn("Servidor offline - usando valores padrão.");
        data = { ram: 0 };
    }

    const level = Math.max(1, Math.min(5, Math.ceil(data.ram / 20)));
    pipboyElement.src = `images/${theme}/pip${level}.png`;
}

updateImage()

setInterval(updateImage, 2000)