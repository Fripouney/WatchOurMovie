import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-profil',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  username: string = '';
  email: string = '';
  password: string = '';
  confirmPassword: string = '';
  oldPassword: string = '';

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.getUserInfo();
  }

  async getUserInfo(): Promise<void> {
    // À implémenter
    return;
  }

  async updateUserInfo(event: Event): Promise<void> {
    event.preventDefault();
    return;
  }

  async updatePassword(event: Event): Promise<void> {
    // À implémenter
    return;
  }

  async deleteAccount(): Promise<void> {
    // À implémenter
    return;
  }
}
