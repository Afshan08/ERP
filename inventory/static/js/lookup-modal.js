class LookupModal {
  constructor(options) {
    this.endpoint = options.endpoint;
    this.model = options.model;
    this.fieldId = options.fieldId;
    this.columns = options.columns;
    this.title = options.title;
    this.data = [];
    this.filteredData = [];
    this.modal = null;
    this.searchInput = null;
    this.tableBody = null;
    this.init();
  }

  init() {
    this.createModal();
    this.attachEventListeners();
  }

  createModal() {
    // Create modal HTML
    const modalHTML = `
      <div id="lookupModal-${this.model}" class="lookup-modal" style="display: none;">
        <div class="lookup-modal-content">
          <div class="lookup-modal-header">
            <h3>${this.title}</h3>
            <span class="lookup-modal-close">&times;</span>
          </div>
          <div class="lookup-modal-body">
            <input type="text" id="lookupSearch-${this.model}" class="lookup-search-input" placeholder="Type to search...">
            <div class="lookup-table-container">
              <table class="lookup-table">
                <thead>
                  <tr id="lookupHeader-${this.model}"></tr>
                </thead>
                <tbody id="lookupBody-${this.model}"></tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);
    this.modal = document.getElementById(`lookupModal-${this.model}`);
    this.searchInput = document.getElementById(`lookupSearch-${this.model}`);
    this.tableBody = document.getElementById(`lookupBody-${this.model}`);
  }

  attachEventListeners() {
    // Close button
    this.modal.querySelector('.lookup-modal-close').addEventListener('click', () => this.close());

    // Click outside to close
    this.modal.addEventListener('click', (e) => {
      if (e.target === this.modal) this.close();
    });

    // Search input
    this.searchInput.addEventListener('input', () => this.filterData());

    // Attach to all lookup buttons for this model
    const lookupButtons = document.querySelectorAll(`button[data-lookup-model="${this.model}"]`);
    lookupButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        this.currentFieldId = e.target.getAttribute('data-field-id') || this.fieldId;
        this.open();
      });
    });
  }

  async open() {
    this.modal.style.display = 'block';
    await this.loadData();
    this.renderTable();
  }

  close() {
    this.modal.style.display = 'none';
  }

  async loadData() {
    try {
      const response = await fetch(this.endpoint);
      if (!response.ok) throw new Error('Failed to load data');
      this.data = await response.json();
      this.filteredData = [...this.data];
    } catch (error) {
      console.error('Error loading lookup data:', error);
      this.data = [];
      this.filteredData = [];
    }
  }

  filterData() {
    const searchTerm = this.searchInput.value.toLowerCase();
    this.filteredData = this.data.filter(item =>
      this.columns.some(col =>
        String(item[col] || '').toLowerCase().includes(searchTerm)
      )
    );
    this.renderTable();
  }

  renderTable() {
    // Render header
    const headerRow = document.getElementById(`lookupHeader-${this.model}`);
    headerRow.innerHTML = this.columns.map(col =>
      `<th>${col.replace(/_/g, ' ').toUpperCase()}</th>`
    ).join('');

    // Render body
    this.tableBody.innerHTML = this.filteredData.map(item => `
      <tr onclick="lookupModals['${this.model}'].selectItem(${item.id})">
        ${this.columns.map(col => `<td>${item[col] || ''}</td>`).join('')}
      </tr>
    `).join('');
  }

  selectItem(id) {
    const fieldId = this.currentFieldId || this.fieldId;
    const selectElement = document.getElementById(fieldId);
    if (selectElement) {
      selectElement.value = id;
      // Trigger change event if needed
      selectElement.dispatchEvent(new Event('change'));
    }
    this.close();
  }
}

// Global registry for lookup modals
// Global registry for lookup modals
window.lookupModals = window.lookupModals || {};
