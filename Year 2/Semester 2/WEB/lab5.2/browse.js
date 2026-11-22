let currentPage = 1;
const limit = 4;

function loadRooms(page = 1) {
    currentPage = page;

    let category = document.getElementById("category").value;
    let beds = document.getElementById("beds").value;
    let price = document.getElementById("price").value;

    // send req to php - url
    fetch(`browse.php?ajax=1&page=${page}&category=${category}&beds=${beds}&price=${price}`)
        // wait for the result and then do stuff
        .then(res => res.json())
        .then(data => {
            // data looks like {rooms: [...] total: 20}
            renderRooms(data.rooms);
            updatePagination(data.total);
        });
}

function renderRooms(rooms) {
    let container = document.getElementById("rooms");
    container.innerHTML = "";

    if (rooms.length === 0) {
        container.innerHTML = "<p>No rooms found</p>";
        return;
    }

    rooms.forEach(room => {
        let div = document.createElement("div");

        div.innerHTML = `
            <h3>Room ID: ${room.id}</h3>
            <p>Beds: ${room.nb_beds}</p>
            <p>Category: ${room.category}</p>
            <p>Price: ${room.price}</p>
            <hr>
        `;

        container.appendChild(div);
    });
}

function updatePagination(total) {
    let nextBtn = document.getElementById("next");
    let prevBtn = document.getElementById("prev");

    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = currentPage * limit >= total;
}

function nextPage() {
    loadRooms(currentPage + 1);
}

function prevPage() {
    if (currentPage > 1) {
        loadRooms(currentPage - 1);
    }
}
