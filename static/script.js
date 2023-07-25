document.addEventListener("DOMContentLoaded", function () {
    const colorSelect = document.getElementById("color");
    const animationSelect = document.getElementById("animation");
    const originalImg = document.getElementById("original-img");
    const sketchImg = document.getElementById("sketch-img");
  
    colorSelect.addEventListener("change", applyColor);
    animationSelect.addEventListener("change", applyAnimation);
  
    function applyColor() {
      const color = colorSelect.value;
      if (color === "original") {
        sketchImg.src = "{{ sketch_path }}"; // Revert to the original sketch
      } else {
        sketchImg.src = "{{ url_for('static', filename='sketch_' + color + '_' + file.filename) }}";
      }
    }
  
    function applyAnimation() {
      const animation = animationSelect.value;
      sketchImg.classList.remove("fadeIn", "zoomIn"); // Remove all animation classes
  
      if (animation !== "none") {
        sketchImg.classList.add(animation); // Apply the selected animation
      }
    }
  });
  