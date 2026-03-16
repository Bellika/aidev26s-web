import { useState, useEffect } from 'react';
import { getAllUsers } from '../services/api';
import { User } from '../types/user';
import './UserList.css';

export default function UserList() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadUsers();
  }, []);

  const loadUsers = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await getAllUsers();
      setUsers(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load users');
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('sv-SE', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return <div className="user-list"><p className="loading">Loading users...</p></div>;
  }

  if (error) {
    return (
      <div className="user-list">
        <p className="error-message">{error}</p>
        <button onClick={loadUsers}>Try Again</button>
      </div>
    );
  }

  return (
    <div className="user-list">
      <div className="header">
        <h2>All Users</h2>
        <button onClick={loadUsers} className="refresh-btn">Refresh</button>
      </div>

      {users.length === 0 ? (
        <p className="no-users">No users found. Create your first user!</p>
      ) : (
        <div className="users-grid">
          {users.map((user) => (
            <div key={user.id} className="user-card">
              <h3>{user.username}</h3>
              <div className="user-details">
                <p><strong>ID:</strong> {user.id}</p>
                <p><strong>Created:</strong> {formatDate(user.created_at)}</p>
                <p><strong>Updated:</strong> {formatDate(user.updated_at)}</p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
