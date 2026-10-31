(() => {
  const sidebar = document.querySelector('.sidebar:not(.sidebar-home) .sidebar-inner');
  if (!sidebar) return;

  // The top follows the header until it sticks; the bottom stays 20px above
  // the viewport edge. A max-height alone leaves no space for margin-top:auto.
  const updateHeight = () => {
    sidebar.style.setProperty('--sidebar-top', `${sidebar.getBoundingClientRect().top}px`);
  };
  let pending = false;
  const scheduleUpdate = () => {
    if (pending) return;
    pending = true;
    requestAnimationFrame(() => {
      updateHeight();
      pending = false;
    });
  };

  addEventListener('scroll', scheduleUpdate, { passive: true });
  addEventListener('resize', scheduleUpdate);
  updateHeight();
})();
