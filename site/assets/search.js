(() => {
  const results = document.getElementById('search-results');
  if (!results) return;
  const query = new URLSearchParams(location.search).get('q')?.trim() || '';
  const input = document.getElementById('search-input');
  input.value = query;
  const status = document.getElementById('search-status');
  if (!query) { status.textContent = 'Enter a subject, ticker, or phrase to search the encyclopedia.'; return; }
  document.title = `Search: ${query} — Chainlore`;
  fetch('/search-index.json').then(response => {
    if (!response.ok) throw new Error('Search unavailable');
    return response.json();
  }).then(pages => {
    const terms = query.toLowerCase().split(/\s+/);
    const matches = pages.filter(page => terms.every(term => `${page.title} ${page.ticker} ${page.text}`.toLowerCase().includes(term)));
    matches.sort((a, b) => Number(b.title.toLowerCase().includes(query.toLowerCase()) || b.ticker.toLowerCase() === query.toLowerCase()) - Number(a.title.toLowerCase().includes(query.toLowerCase()) || a.ticker.toLowerCase() === query.toLowerCase()));
    status.textContent = `${matches.length} ${matches.length === 1 ? 'article' : 'articles'} found for “${query}”.`;
    for (const page of matches) {
      const item = document.createElement('li');
      const heading = document.createElement('h2');
      const link = document.createElement('a');
      link.href = page.url;
      link.textContent = page.title;
      const excerpt = document.createElement('p');
      excerpt.textContent = page.description;
      heading.append(link); item.append(heading, excerpt); results.append(item);
    }
    if (!matches.length) {
      const hint = document.createElement('p');
      hint.textContent = 'Try another term, or browse all articles below.';
      results.append(hint);
    }
  }).catch(() => { status.textContent = 'Search could not load. Please try again or browse all articles below.'; });
})();
