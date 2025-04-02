document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("darkModeToggle");
    const body = document.body;
    const modeText = document.getElementById("modeText"); // Ensure this element exists

    if (!toggleButton || !modeText) {
        console.error("Dark mode toggle button or modeText element not found!");
        return;
    }

    // Check Local Storage for Dark Mode Preference
    const isDarkMode = localStorage.getItem("darkMode") === "enabled";

    if (isDarkMode) {
        body.classList.add("dark-mode");
        modeText.textContent = "Light Mode"; // Update text
    } else {
        modeText.textContent = "Dark Mode";
    }

    // Toggle Dark Mode on Button Click
    toggleButton.addEventListener("click", function () {
        if (body.classList.contains("dark-mode")) {
            body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
            modeText.textContent = "Dark Mode"; // Update text
        } else {
            body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
            modeText.textContent = "Light Mode"; // Update text
        }
    });
});
