let championsData = [];

async function fetchChampions() {
    try {
        const response = await fetch('http://localhost:3000/api/champions', { method: "GET" });
        championsData = await response.json();
        displayChampions(championsData);
    } catch (error) {
        console.error('Error fetching champions:', error);
    }
}

function displayChampions(data) {
    const container = document.getElementById('champions-container');
    container.innerHTML = '';

    data.forEach(champion => {
        const championDiv = document.createElement('div');
        championDiv.className = 'champion';
        championDiv.innerHTML = `
            <div class="champion-name">${champion.name}</div>
            <div class="champion-role">${champion.role}</div>
            <div class="champion-tier">${champion.tier}</div>
            <div class="champion-win-rate">${champion.win_rate}</div>
            <div class="champion-pick-rate">${champion.pick_rate}</div>
            <div class="champion-ban-rate">${champion.ban_rate}</div>
            <div class="champion-matches">${champion.matches}</div>
        `;
        container.appendChild(championDiv);
    });
}

function filterChampions() {
    const searchValue = document.getElementById('champion-search').value.toLowerCase();
    const filteredData = championsData.filter(champion =>
        champion.name.toLowerCase().includes(searchValue)
    );
    displayChampions(filteredData);
}

document.getElementById('champion-search').addEventListener('input', filterChampions);

// Call the function to fetch and display champions data
fetchChampions();