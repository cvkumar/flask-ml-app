import {Component} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Predict Iris Flower with SVM Model';
  model_accuracy = 0;
  modelTrained = false;

  prediction = null;

  sepal_length: number = null;
  sepal_width: number = null;
  petal_length: number = null;
  petal_width: number = null;

  results = null;
  displayedColumns = ['time', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'prediction'];

  constructor(private http: HttpClient) {
  }

  public trainModel() {
    return this.http.get('http://localhost:5000/train').subscribe((response: any) => {
      // console.log(response);
      this.model_accuracy = response.model_accuracy;
      console.log(this.model_accuracy);
      this.modelTrained = true;
    });
  }

  public makePrediction() {
    let headers = new HttpHeaders();
    headers = headers.append('Content-Type', 'application/json');
    const payload = JSON.stringify({
      'sepal_length': this.sepal_length,
      'sepal_width': this.sepal_width,
      'petal_length': this.petal_length,
      'petal_width': this.petal_width
    });

    return this.http.post('http://localhost:5000/predict', payload, {'headers': headers}).subscribe((response: any) => {
      this.prediction = response.prediction;
      console.log(this.prediction);
    });
  }

  public getPredictions() {
    return this.http.get('http://localhost:5000/predictions').subscribe((response: any) => {
      this.results = response.predictions;
      console.log(response);
    });
  }

  public deletePredictions() {
    return this.http.delete('http://localhost:5000/predictions').subscribe((response: any) => {
      this.results = [];
      console.log(response);
    });
  }

  private fieldsFilled(): boolean {
    return this.sepal_length != null && this.sepal_width != null && this.petal_length != null && this.petal_width != null;
  }

}
