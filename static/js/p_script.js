document.addEventListener("DOMContentLoaded", function() {
    let searchInput = document.getElementById("searchInput");
    if (!searchInput) return;

    searchInput.addEventListener("keyup", function() {
        let filter = searchInput.value.toLowerCase();
        let rows = document.querySelectorAll("tbody tr");

        rows.forEach(row => {
            let name = row.cells[1].textContent.toLowerCase();
            row.style.display = name.includes(filter) ? "" : "none";
        });
    });
});

