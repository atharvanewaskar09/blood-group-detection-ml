function predict(event) {
  event.preventDefault();   // HARD STOP refresh

  const fileInput = document.getElementById("fileInput");
  const result = document.getElementById("result");

  if (!fileInput.files.length) {
    result.innerText = "❌ Please select an image";
    return false;
  }

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);

  result.innerText = "⏳ Predicting...";

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      if (data.blood_group) {
        result.innerText = "✅ Prediction: " + data.blood_group;
      } else {
        result.innerText = "❌ Error: " + data.error;
      }
    })
    .catch(() => {
      result.innerText = "❌ Backend not reachable";
    });

  return false; // 🚨 ABSOLUTE STOP
}