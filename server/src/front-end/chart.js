document.getElementById('chart-select').addEventListener('change', function() {
    var value = this.value;
    var charts = document.querySelectorAll('.chart');
    charts.forEach(function(chart) {
        if (chart.id === value) {
            chart.classList.add('show');
        } else {
            chart.classList.remove('show');
        }
    });
});

// Function to convert rate percentage string to number
const parseRate = (rate) => parseFloat(rate.replace('%', ''));
// Function to convert matches string to number
const parseMatches = (matches) => parseInt(matches.replace(/,/g, ''), 10);

// Function to render the box plot using Plotly
const renderBoxPlots = (champions) => {
    const roles = {};

    champions.forEach(champ => {
        const role = champ.role;
        const matches = parseMatches(champ.matches);
        const winRate = parseRate(champ.win_rate);
        const pickRate = parseRate(champ.pick_rate);
        const banRate = parseRate(champ.ban_rate);

        if (isNaN(winRate) || isNaN(pickRate) || isNaN(banRate) || isNaN(matches)) {
            throw new Error(`Invalid matches or rate value(s): ${champ.matches}, ${champ.win_rate}, ${champ.pick_rate}, ${champ.ban_rate}`);
        }

        if (!roles[role]) {
            roles[role] = { matches: [], winRates: [], pickRates: [], banRates: [] };
        }

        roles[role].matches.push(matches);
        roles[role].winRates.push(winRate);
        roles[role].pickRates.push(pickRate);
        roles[role].banRates.push(banRate);
    });

    // Prepare data for Plotly
    const matchesData = Object.keys(roles).map(role => ({
        y: roles[role].matches,
        type: 'box',
        name: role
    }));

    const winRateData = Object.keys(roles).map(role => ({
        y: roles[role].winRates,
        type: 'box',
        name: role
    }));

    const pickRateData = Object.keys(roles).map(role => ({
        y: roles[role].pickRates,
        type: 'box',
        name: role
    }));

    const banRateData = Object.keys(roles).map(role => ({
        y: roles[role].banRates,
        type: 'box',
        name: role
    }));

    // Function to get CSS variable values
    function getCssVariable(varName) {
        return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
    }

    // Função para converter hexadecimal para rgba com opacidade
    function hexToRgba(hex, alpha) {
        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);
        return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    }

    // Define the layout for the plots with font customization
    const layout = (title, yaxisTitle) => ({
        title: {
            text: title,
            font: {
                size: parseInt(getCssVariable('--title-size'), 10), // Font size for the title
                family: getCssVariable('--font-family'), // Font family for the title
                color: getCssVariable('--text-color') // Font color for the title
            }
        },
        yaxis: {
            title: {
                text: yaxisTitle,
                font: {
                    size: parseInt(getCssVariable('--text-size'), 10), // Font size for the y-axis title
                    family: getCssVariable('--font-family'), // Font family for the y-axis title
                    color: getCssVariable('--text-color') // Font color for the y-axis title
                }
            },
            tickfont: {
                size: parseInt(getCssVariable('--text-size'), 10), // Font size for y-axis tick labels
                family: getCssVariable('--font-family'), // Font family for y-axis tick labels
                color: getCssVariable('--text-color') // Font color for y-axis tick labels
            },
            gridcolor: hexToRgba(getCssVariable('--text-color'), 0.1), // Cor da grade do eixo y com 50% de opacidade
            zeroline: false
        },
        xaxis: {
            title: {
                text: 'Role',
                font: {
                    size: parseInt(getCssVariable('--text-size'), 10), // Font size for the x-axis title
                    family: getCssVariable('--font-family'), // Font family for the x-axis title
                    color: getCssVariable('--text-color') // Font color for the x-axis title
                }
            },
            tickfont: {
                size: parseInt(getCssVariable('--text-size'), 10), // Font size for x-axis tick labels
                family: getCssVariable('--font-family'), // Font family for x-axis tick labels
                color: getCssVariable('--text-color') // Font color for x-axis tick labels
            }
        },
        legend: {
            font: {
                size: parseInt(getCssVariable('--text-size'), 10), // Tamanho da fonte da legenda
                family: getCssVariable('--font-family'), // Família da fonte da legenda
                color: getCssVariable('--text-color') // Cor da fonte da legenda
            }
        },
        plot_bgcolor: getCssVariable('--box-color'),
        paper_bgcolor: getCssVariable('--background-color')
    });

    // Render the plots
    Plotly.newPlot('matches-plot', matchesData, layout('Box Plot', 'Matches'));
    Plotly.newPlot('win-rate-plot', winRateData, layout('Box Plot', 'Win Rate (%)'));
    Plotly.newPlot('pick-rate-plot', pickRateData, layout('Box Plot', 'Pick Rate (%)'));
    Plotly.newPlot('ban-rate-plot', banRateData, layout('Box Plot', 'Ban Rate (%)'));
};

// Main function to fetch champion data from the API and display the plots
const fetchChampionData = async () => {
    try {
        const response = await fetch('http://localhost:3000/api/champions', { method: "GET" });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const champions = await response.json();
        renderBoxPlots(champions);  // Call the display function here
    } catch (error) {
        console.error('Error fetching champion data:', error);
    }
};

// Execute the main function
fetchChampionData();