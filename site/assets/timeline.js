(() => {
  const input = document.getElementById('timeline-filter');
  if (input) {
    const form = input.form;
    const count = document.getElementById('timeline-count');
    const items = [...document.querySelectorAll('.timeline li')].map(item => ({ item, text: item.textContent.toLowerCase() }));
    const sections = [...document.querySelectorAll('.timeline-section')];
    const apply = () => {
      const query = input.value.trim();
      const terms = query.toLowerCase().split(/\s+/);
      let shown = 0;
      for (const { item, text } of items) {
        item.hidden = !terms.every(term => text.includes(term));
        if (!item.hidden) shown += 1;
      }
      for (const section of sections) section.hidden = !section.querySelector('li:not([hidden])');
      count.textContent = `${shown} of ${items.length} events`;
      // A filtered view keeps its own URL, so it can be shared.
      const url = new URL(location.href);
      if (query) url.searchParams.set('q', query); else url.searchParams.delete('q');
      history.replaceState(null, '', url);
    };
    form.hidden = false;
    form.addEventListener('submit', event => event.preventDefault());
    input.addEventListener('input', apply);
    input.value = new URLSearchParams(location.search).get('q') || '';
    apply();
  }

  const today = document.getElementById('on-this-day-today');
  if (today) {
    const now = new Date();
    const link = document.querySelector(`[data-day="${now.getMonth() + 1}-${now.getDate()}"]`);
    const label = now.toLocaleDateString('en-GB', { day: 'numeric', month: 'long' });
    document.getElementById('today').textContent = `Today, ${label}`;
    today.hidden = false;
    if (!link) {
      today.append(Object.assign(document.createElement('p'), { textContent: 'Nothing is recorded for this date yet.' }));
      return;
    }
    link.classList.add('today');
    fetch(link.href).then(response => {
      if (!response.ok) throw new Error('Day unavailable');
      return response.text();
    }).then(page => {
      today.append(new DOMParser().parseFromString(page, 'text/html').querySelector('ol.timeline'));
    }).catch(() => { today.hidden = true; });
  }
})();
