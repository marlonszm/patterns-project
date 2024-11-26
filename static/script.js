document.addEventListener("DOMContentLoaded", function () {
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-info");

    tabButtons.forEach(button => {
        button.addEventListener("click", function () {
            // Remove active class from all buttons
            tabButtons.forEach(btn => btn.classList.remove("active"));
            // Remove active class from all tab contents
            tabContents.forEach(content => content.classList.remove("active"));

            // Add active class to the clicked button
            this.classList.add("active");

            // Show the corresponding tab content
            const target = this.getAttribute("data-target");
            const targetContent = document.querySelector(target);
            if (targetContent) {
                targetContent.classList.add("active");
            }
        });
    });

    // Show the first tab by default
    if (tabButtons.length > 0 && tabContents.length > 0) {
        tabButtons[0].classList.add("active");
        tabContents[0].classList.add("active");
    }
});
