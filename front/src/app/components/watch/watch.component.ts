import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import axios from 'axios';

@Component({
  selector: 'app-watch',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './watch.component.html'
})
export class WatchComponent implements OnInit {
  friends: any[] = [];
  selectedFriends: number[] = [];
  movies: any[] = [];
  suggestions: any[] = [];
  error = '';
  token = localStorage.getItem('token');
  userId: number | null = null;

  tmdbToken = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YzYyOGQ3MmNiODAwMzNhOTAxNzgwNjdiMGU0MTk2OSIsIm5iZiI6MTczNzEwNTE1Ni40MzkwMDAxLCJzdWIiOiI2NzhhMWYwNDM4OTIwMzkzYWQxZDZmNWIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.tCeVDHw3sWQc8LkD1Yh308oexhQOXhtkNNd9i73e-y8';

  ngOnInit() {
    if (!this.token) return;
    this.fetchUserId();
  }

  async fetchUserId() {
    try {
      const res = await axios.get('http://localhost:8000/me', {
        headers: { Authorization: `Bearer ${this.token}` }
      });
      this.userId = res.data.id;
      this.fetchFriends();
      this.fetchMoviesFromTMDB();
    } catch (err) {
      this.error = "Erreur récupération utilisateur";
    }
  }

  async fetchFriends() {
    try {
      const res = await axios.get(`http://localhost:8000/user/${this.userId}/friends`, {
        headers: { Authorization: `Bearer ${this.token}` }
      });
      this.friends = res.data.friends;
    } catch (err) {
      this.error = "Erreur chargement amis";
    }
  }

  async fetchMoviesFromTMDB() {
    try {
      const res = await axios.get("https://api.themoviedb.org/3/movie/popular?language=fr", {
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${this.tmdbToken}`
        }
      });
      this.movies = res.data.results;
    } catch (err) {
      this.error = "Erreur chargement films TMDB";
    }
  }

  toggleFriend(id: number) {
    if (this.selectedFriends.includes(id)) {
      this.selectedFriends = this.selectedFriends.filter(f => f !== id);
    } else {
      this.selectedFriends.push(id);
    }
  }

  async getSuggestions() {
    try {
      const movieIds = this.movies.map(m => m.id);
      const users = [...this.selectedFriends, this.userId!];
  
      const res = await axios.post('http://localhost:8000/watch/suggestions', {
        users,
        movies: movieIds
      }, {
        headers: { Authorization: `Bearer ${this.token}` }
      });
  
      const suggestionIds = res.data;
  
      // Requête TMDB pour chaque film
      const details = await Promise.all(suggestionIds.map((id: number) =>
        axios.get(`https://api.themoviedb.org/3/movie/${id}?language=fr`, {
          headers: {
            Accept: "application/json",
            Authorization: `Bearer ${this.tmdbToken}`
          }
        }).then(r => r.data)
      ));
  
      this.suggestions = details;
    } catch (err) {
      this.error = "Erreur lors de la récupération des suggestions.";
      console.error(err);
    }
  }  
}
