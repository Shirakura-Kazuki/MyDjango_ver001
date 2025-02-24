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

/* ------------ID:3(フィルター開閉処理)------------- */
// document.addEventListener("DOMContentLoaded", function () {
//     let filterToggle = document.getElementById("filterToggle");
//     let filterMenu = document.getElementById("filterMenu");
//     let closeFilter = document.getElementById("closeFilter");

//     // 🔹 フィルター開く
//     filterToggle.addEventListener("click", function () {
//         filterMenu.classList.add("show");
//     });

//     // 🔹 フィルター閉じる
//     closeFilter.addEventListener("click", function () {
//         filterMenu.classList.remove("show");
//     });

//     // 🔹 フィルター外をクリックしたら閉じる
//     document.addEventListener("click", function (event) {
//         if (!filterMenu.contains(event.target) && !filterToggle.contains(event.target)) {
//             filterMenu.classList.remove("show");
//         }
//     });
// });


document.addEventListener("DOMContentLoaded", function () {
    let filterToggle = document.getElementById("filterToggle");
    let filterMenu = document.getElementById("filterMenu");
    let closeFilter = document.getElementById("closeFilter");

    // 🔹 フィルター開閉処理
    filterToggle.addEventListener("click", function () {
        filterMenu.classList.toggle("show");
    });

    closeFilter.addEventListener("click", function () {
        filterMenu.classList.remove("show");
    });

    // 🔹 フィルター外クリックで閉じる
    document.addEventListener("click", function (event) {
        if (!filterMenu.contains(event.target) && !filterToggle.contains(event.target)) {
            filterMenu.classList.remove("show");
        }
    });
});
