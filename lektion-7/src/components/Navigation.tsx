import './Navigation.css';

interface NavigationProps {
  currentPage: 'create' | 'list';
  onNavigate: (page: 'create' | 'list') => void;
}

export default function Navigation({ currentPage, onNavigate }: NavigationProps) {
  return (
    <nav className="navigation">
      <h1>User Management</h1>
      <div className="nav-links">
        <button
          className={currentPage === 'create' ? 'active' : ''}
          onClick={() => onNavigate('create')}
        >
          Create User
        </button>
        <button
          className={currentPage === 'list' ? 'active' : ''}
          onClick={() => onNavigate('list')}
        >
          All Users
        </button>
      </div>
    </nav>
  );
}
