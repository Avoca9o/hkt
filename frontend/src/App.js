import React, { useState, useEffect} from 'react';
import './App.css';

const App = () => {

  const BACKEND_URL = 'http://0.0.0.0:80';
  const [session_id, setSessionId] = useState('123456789');

  const [searchResults, setSearchResults] = useState([])

  const requestCashbacks = async (request) => {
      try {
        const search_url = `${BACKEND_URL}/search`;
        const data = request;
        const response = await fetch(search_url, {
          method: 'POST',
          body: JSON.stringify(data),
          headers: { 'Content-Type': 'application/json' },
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const searchData = await response.json();

        setSearchResults(searchData.map((result, index) => ({
          header: result.header,
          description: result.description,
          cashback_logo: `data:image/png;base64,${result.image}`,
          bank_logo: `data:image/png;base64,${result.bank_image}`
        })));
      } catch (error) {
        console.error('Error fetching or resizing images:', error);
      }
    };

  /* Initial Data Fetch */
  useEffect(() => {
    const fetchData = async () => {
      const defaultRequest = { "session_id": session_id};
      await requestCashbacks(defaultRequest);
    };
    fetchData();
  }, []);
  
  const handleSearch = async () => {
    const request = { "session_id": session_id, "text": searchTerm };
    await requestCashbacks(request);
  };

  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    if (searchTerm) {
      handleSearch();
    }
  }, [searchTerm]);

  const [categories, setCategories] = useState(['Продукты',
                                                'Одежда',
                                                'Техника',
                                                'Настольные игры',
                                                'Косметика',
                                                'Путешествия',
                                                'Супермаркеты',
                                                'Дом и ремонт',
                                                'Заправки',
                                                'Аптеки']);

  const [isMiniWindowOpen, setIsMiniWindowOpen] = useState(false);

  const handleClose = () => {
    setIsMiniWindowOpen(false);
    document.body.style.overflowY = '';
  };

  const openMiniWindow = (description) => {
    setIsMiniWindowOpen(true);
    const miniWindow = document.createElement('div');
    miniWindow.className = 'mini-window';
    miniWindow.innerHTML = `
      <style>
        .mini-window {
          position: fixed;
          top: 18%;
          left: 37%;
          right: 25%;
          bottom: 38%;
          font-size: 24px; 
          display: flex;
          justify-content: center;
          align-items: center; 
        }
        .close-btn {
          position: absolute;
          top: 10px;
          right: 10px;
          cursor: pointer;
          width: 40px;
          height: 40px;
          font-size: 24px; 
        }
      </style>
      <p>${description}</p>
      <button class="close-btn">X</button>
    `;

    document.body.appendChild(miniWindow);

    const closeBtn = miniWindow.querySelector('.close-btn');
    closeBtn.addEventListener('click', () => {
      setIsMiniWindowOpen(false);
      miniWindow.remove();
    });

    // Prevent scrolling on the page behind the mini-window
    document.body.style.overflowY = 'hidden';
  };

  return (
    <div className="app-container">

      {/* Search Bar */}
      <div className="search-bar" >
        <button onClick={handleSearch}>
          Search
        </button>
        <span>
          <input
            type="text"
            placeholder="Search cashbacks..."
            onChange={(e) => {setSearchTerm(e.target.value);}}
            value={searchTerm}
            onKeyDown={(e) => {
              if (e.key === 'Enter') {
                setSearchTerm(e.target.value);
              };
            }}
            width="10%"
          />
        </span>
      </div>
   
      {/* Search Area and Categories Container */}
      <div className="search-category-container">
        {/* Category Area */}
        <div className="category-area">
          {categories.map((category, index) => (
            <div
            key={index}
            className="category-button"
            onClick={() => {
              setSearchTerm(category)
            }}
          >
            <p>{category}</p>
          </div>
          ))}
        </div>

        {/* Search Results Area */}
        <div className="search-results-area">
          {searchResults.map(result => (
            <div key={result.description} className="result-box-area"  style={{position: 'relative'}}
            onClick={(e) => {
              const rect = e.currentTarget.getBoundingClientRect();
              openMiniWindow(result.description);
            }}>
              {/* Left Logo */}
              <div className='left-logo'>
                <img src={result.cashback_logo}/>
              </div>

              {/* Card Header */}
              <div className='card-header'>
                <p>{result.header}</p>
              </div>

              {/* Right Logo */}
              <div className='right-logo'>
                <img src={`${result.bank_logo}`} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
