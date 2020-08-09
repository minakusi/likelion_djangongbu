const h22 = document.getElementById("h22");

h22.addEventListener("mouseover", function() {
    r = Math.ceil(Math.random() * 200);
    g = Math.ceil(Math.random() * 200);
    b = Math.ceil(Math.random() * 200);
    h22.style.color = `rgb(${r},${g},${b})`;
});