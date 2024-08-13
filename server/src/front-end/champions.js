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

        // Add click event to fill the form
        championDiv.addEventListener('click', () => {
            document.getElementById('champion-search').value = champion.name;
            document.getElementById('tier').value = champion.tier;
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
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

function isChampionValid(championName) {
    return championsData.some(champion => champion.name.toLowerCase() === championName.toLowerCase());
}

document.getElementById('alert-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const champion = document.getElementById('champion-search').value.trim();
    const email = document.getElementById('email').value.trim();
    const tier = document.getElementById('tier').value.trim();
    
    if (!champion || !email || !tier) {
        alert('Please fill in all fields.');
        return;
    }

    if (!isChampionValid(champion)) {
        alert(`The champion ${champion} does not exist.`);
        return;
    }

    // Simple email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    console.log(`Champion: ${champion}, Email: ${email}, Tier: ${tier}`);
    
    const data = {
        champion: champion,
        email: email,
        tier: tier
    };

    try {
        const response = await fetch('/champions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            alert('Data submitted successfully!');
        } else {
            alert('Error submitting data. Please try again.');
        }
    } catch (error) {
        console.error('Network error:', error);
        alert('Error submitting data. Check your connection and try again.');
    }
});
