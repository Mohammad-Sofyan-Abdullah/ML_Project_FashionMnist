async function submitData() {
  const rawPixels = document.getElementById("pixels").value.trim();
  const pixelArray = rawPixels.split(',').map(Number);
  const model = document.getElementById("model").value;

  if (pixelArray.length !== 64) {
    alert("You must enter exactly 64 values.");
    return;
  }

  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pixels: pixelArray, model_name: model })
  });

  const result = await response.json();
  document.getElementById("result").textContent = `Prediction: ${result.prediction}`;
}
