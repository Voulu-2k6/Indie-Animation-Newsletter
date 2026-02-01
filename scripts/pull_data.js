fetch("../../articles.json")
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
      <h2><a href="${item.url}" target="_blank">${item.title}</a></h2>
    `;

    home.appendChild(div);
  });
}