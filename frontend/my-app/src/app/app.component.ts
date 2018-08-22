import {Component} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {RequestOptions} from '@angular/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Iris Prediction Modeling';

  constructor(private http: HttpClient) {
    // this.trainModel();
  }

  public trainModel() {
    return this.http.get('/train').subscribe((data: any) => {
      console.log(data);
    });
  }

  public makePrediction() {
    let headers = new HttpHeaders();
    headers = headers.append('Content-Type', 'application/json');
    // console.log(headers);
    const payload = JSON.stringify({'sepal_length': 5, 'sepal_width': 3, 'petal_length': 1, 'petal_width': 1});

    return this.http.post('/predict', payload, {'headers': headers}).subscribe((data: any) => {
      console.log(data);
    });
  }

  public getPredictions() {
    return this.http.get('/predictions').subscribe((data: any) => {
      console.log(data);
    });
  }

  public deletePredictions() {
    return this.http.delete('/predictions').subscribe((data: any) => {
      console.log(data);
    });
  }
}
