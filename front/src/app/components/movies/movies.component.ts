import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import axios from 'axios';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-movies',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './movies.component.html',
})
export class MoviesComponent implements OnInit {
  url = "https://api.themoviedb.org/3";
  error = '';
  movies: any[] = [];
  filteredMovies: any[] = []
  allGenres: any[] = []
  selectedGenres: number[] = []
  link = "https://api.themoviedb.org/3/movie/popular?language=fr&page=1";
  tmdbToken = environment.tmdbToken;

  constructor(private router: Router) {}

  // Récupère la liste des films populaires du moment
  // Il peut y avoir plusieurs pages, est-ce nécessaire ?
  async getPopularMovies() {
    try {
      const response = await axios.get(`${this.url}/movie/popular?language=fr&page=1`, {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${this.tmdbToken}`
        }
      });
      this.movies = response.data.results;
      this.filteredMovies = this.movies;
    } catch(error) {
      this.error = "Erreur lors de la récupération des films";
    }
  }

  async getAllGenres() {
    try {
      const response = await axios.get(`${this.url}/genre/movie/list?language=fr`, {
        method: 'GET',
        headers: {
          Accept: 'application/json',
          Authorization: `Bearer ${this.tmdbToken}`
        }
      });
      this.allGenres = response.data.genres;
    } catch (error) {
      this.error = "Erreur lors de la récupération des genres de films";
    }
  }

  // Affiche seulement les films contenant un des genres sélectionnés
  filterMovies() {
    if(this.selectedGenres.length === 0) {
      console.log("???");
      this.filteredMovies = this.movies;
    } else {
      console.log(this.selectedGenres);
      this.filteredMovies = this.movies.filter(movie => 
        movie.genre_ids.some((genreId: number) => this.selectedGenres.includes(genreId))
      );
    }
  }

  // Ajoute ou enlève un filtre en fonction des choix de l'utilisateur
  toggleGenre(genreId: number) {
    console.log(genreId);
    if(this.selectedGenres.includes(genreId)) {
      this.selectedGenres = this.selectedGenres.filter(id => genreId !== id); // Supprimer le genre
    } else {
      this.selectedGenres.push(genreId); // Ajouter le genre
    }
    console.log(this.selectedGenres);
    this.filterMovies();
  }

  async ngOnInit() {
    await this.getPopularMovies();
    await this.getAllGenres();
  }

  // Permet de faire des lignes de 5 films
  getMoviesInRows(): any[][] {
    const rows = [];
    for (let i = 0; i < this.filteredMovies.length; i += 5) {
      rows.push(this.filteredMovies.slice(i, i + 5));
    }
    return rows;
  }

  // Redirige vers la page de détails d'un film
  goToMovieDetails(movieId: number) {
    this.router.navigate(['/films', movieId]);
  }
}
