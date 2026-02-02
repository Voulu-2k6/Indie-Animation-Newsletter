fetch("https://voulu-2k6.github.io/Indie-Animation-Newsletter/articles.JSON")
  .then(response => response.json())
  .then(data => {
    // 'data' is now an array of articles
    populateArticle(data);
  })
  .catch(err => console.error("Error loading articles:", err));

function populateArticle(articles) {
  const home = document.querySelector("article");
  if (!home) return;

  // Clear any existing content
  home.innerHTML = "";
  // Loop through each article and create a div for it
  articles.forEach(item => {
    const div = document.createElement("div");
    div.classList.add("article-item"); // optional CSS class

    div.innerHTML = `
    <div class="item">
      <img src="${item.image}" alt="${item.title}" />
      <div class="item-text">
        <h2>${item.title}</h2>
        <a href="${item.url}" target="_blank">View</a>
        <p class="date">${item.date}</p>
      </div>
    </div>
    `;

    home.appendChild(div);
  });
}