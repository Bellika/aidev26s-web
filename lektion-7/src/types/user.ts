export interface User {
  id: number;
  username: string;
  created_at: string;
  updated_at: string;
}

export interface CreateUserRequest {
  username: string;
  password: string;
}

export interface ApiError {
  detail: string;
}
