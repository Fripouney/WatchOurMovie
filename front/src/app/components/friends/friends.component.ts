import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-friends',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './friends.component.html',
})
export class FriendsComponent implements OnInit {
  newFriendUsername: string = '';
  friends: { id: number; username: string }[] = [];
  pendingRequests: { id: number; username: string }[] = [];
  userId: number = 0;
  token: string | null = null;

  ngOnInit(): void {
    const storedToken = localStorage.getItem('token');
  
    if (!storedToken) {
      alert("Utilisateur non authentifié.");
      return;
    }
  
    this.token = storedToken;
  
    // Récupérer l'ID via /users/me
    fetch('http://localhost:8000/me/', {
      headers: {
        'Authorization': `Bearer ${this.token}`
      }
    })
      .then(res => res.json())
      .then(data => {
        this.userId = data.id;
        this.fetchFriends();
        this.fetchPendingRequests();
      })
      .catch(err => {
        console.error('Erreur utilisateur /me:', err);
      });
  }
  

  async fetchFriends(): Promise<void> {
    try {
      const res = await fetch(`http://localhost:8000/user/${this.userId}/friends`, {
        headers: { 'Authorization': `Bearer ${this.token}` }
      });
      const data = await res.json();
      this.friends = data.friends;
    } catch (err) {
      console.error("Erreur fetchFriends:", err);
    }
  }

  async fetchPendingRequests(): Promise<void> {
    try {
      const res = await fetch(`http://localhost:8000/user/${this.userId}/friend-requests`, {
        headers: { 'Authorization': `Bearer ${this.token}` }
      });
      const data = await res.json();
      this.pendingRequests = data.requests;
    } catch (err) {
      console.error("Erreur fetchPendingRequests:", err);
    }
  }

  async addFriend(event: Event): Promise<void> {
    event.preventDefault();

    const friendId = await this.getUserIdByUsername(this.newFriendUsername);
    if (!friendId) {
      return;
    }

    try {
      const res = await fetch(`http://localhost:8000/user/${this.userId}/friend?friend_id=${friendId}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.token}`
        }
      });

      const data = await res.json();
      this.newFriendUsername = '';
      this.fetchPendingRequests();
    } catch (err) {
      console.error("Erreur addFriend:", err);
    }
  }

  async removeFriend(friendId: number): Promise<void> {
    try {
      const res = await fetch(`http://localhost:8000/user/${this.userId}/friend/${friendId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${this.token}` }
      });

      const data = await res.json();
      this.fetchFriends();
      this.fetchPendingRequests();
    } catch (err) {
      console.error("Erreur removeFriend:", err);
    }
  }

  async declineRequest(friendId: number): Promise<void> {
    try {
      const res = await fetch(`http://localhost:8000/user/${this.userId}/friend/${friendId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${this.token}` }
      });

      const data = await res.json();
      this.fetchPendingRequests();
    } catch (err) {
      console.error("Erreur declineRequest:", err);
    }
  }

  async acceptRequest(friendId: number): Promise<void> {
    try {
      const res = await fetch(`http://localhost:8000/user/${this.userId}/friend/${friendId}/accept`, {
        method: 'PUT',
        headers: { 'Authorization': `Bearer ${this.token}` }
      });

      const data = await res.json();
      this.fetchFriends();
      this.fetchPendingRequests();
    } catch (err) {
      console.error("Erreur acceptRequest:", err);
    }
  }

  async getUserIdByUsername(username: string): Promise<number | null> {
    try {
      const res = await fetch(`http://localhost:8000/user/by-username/${username}`, {
        headers: { 'Authorization': `Bearer ${this.token}` }
      });
      if (!res.ok) {
        return null;
      }

      const data = await res.json();
      return data.id;
    } catch (err) {
      console.error("Erreur getUserIdByUsername:", err);
      return null;
    }
  }
}
