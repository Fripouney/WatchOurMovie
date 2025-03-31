import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import axios from 'axios';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-profil',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profil.component.html',
  styleUrls: ['./profil.component.css']
})
export class ProfilComponent implements OnInit {
  username: string = '';
  password: string = '';
  confirmPassword: string = '';
  oldPassword: string = '';

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.fetchProfile();
  }

  async fetchProfile(): Promise<void> {
    try {
      const token = localStorage.getItem('token');
      const response = await axios.get('http://localhost:8000/me', {
        headers: { Authorization: `Bearer ${token}` }
      });
      this.username = response.data.username;
    } catch (error) {
      alert("Erreur lors du chargement du profil.");
      console.error(error);
    }
  }

  async updateUserInfo(event: Event): Promise<void> {
    event.preventDefault();
    try {
      const token = localStorage.getItem('token');
      await axios.put(
        'http://localhost:8000/me',
        { username: this.username },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert('Username mis à jour');
    } catch (error) {
      alert("Erreur lors de la mise à jour");
      console.error(error);
    }
  }

  async updatePassword(event: Event): Promise<void> {
    event.preventDefault();

    if (this.password !== this.confirmPassword) {
      alert("Les mots de passe ne correspondent pas.");
      return;
    }

    try {
      const token = localStorage.getItem('token');
      await axios.put(
        'http://localhost:8000/me/password',
        {
          old_password: this.oldPassword,
          new_password: this.password
        },
        {
          headers: { Authorization: `Bearer ${token}` }
        }
      );
      alert("Mot de passe mis à jour !");
    } catch (error) {
      alert("Erreur lors du changement de mot de passe.");
      console.error(error);
    }
  }

  async deleteAccount(): Promise<void> {
    try {
      const token = localStorage.getItem('token');
      await axios.delete('http://localhost:8000/me', {
        headers: { Authorization: `Bearer ${token}` }
      });
      alert("Compte supprimé.");
      localStorage.removeItem('token');
      this.router.navigate(['/login']);
    } catch (error) {
      alert("Erreur lors de la suppression du compte.");
      console.error(error);
    }
  }
}
