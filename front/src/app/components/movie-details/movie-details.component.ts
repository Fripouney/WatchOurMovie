import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-movie-details',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './movie-details.component.html',
})
export class MovieDetailsComponent implements OnInit {
  movie: any;
  error = '';

  constructor(private route: ActivatedRoute) {}

  async getMovieDetails(movieId: string) {
    try {
      const response = await axios.get(`https://api.themoviedb.org/3/movie/${movieId}?language=fr`, {
        headers: {
          Accept: "application/json",
          Authorization: "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YzYyOGQ3MmNiODAwMzNhOTAxNzgwNjdiMGU0MTk2OSIsIm5iZiI6MTczNzEwNTE1Ni40MzkwMDAxLCJzdWIiOiI2NzhhMWYwNDM4OTIwMzkzYWQxZDZmNWIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.tCeVDHw3sWQc8LkD1Yh308oexhQOXhtkNNd9i73e-y8"
        }
      });
      this.movie = response.data;
    } catch (error) {
      this.error = "Erreur lors de la récupération du film";
    }
  }

  ngOnInit() {
    const movieId = this.route.snapshot.paramMap.get("id");
    if (movieId) {
      this.getMovieDetails(movieId);
    }
  }
}
