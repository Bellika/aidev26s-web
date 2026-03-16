import { useState } from 'react';
import Navigation from './components/Navigation';
import CreateUser from './components/CreateUser';
import UserList from './components/UserList';
import './App.css';

function App() {
  const [currentPage, setCurrentPage] = useState<'create' | 'list'>('create');

  return (
    <div className="app">
      <Navigation currentPage={currentPage} onNavigate={setCurrentPage} />
      <main className="main-content">
        {currentPage === 'create' ? <CreateUser /> : <UserList />}
      </main>
    </div>
  );
}

export default App;
