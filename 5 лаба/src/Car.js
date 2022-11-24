import React, {Component} from 'react';
import { Link } from 'react-router-dom';


class Car extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            car: [],

        }
        this.pk=1;


    }
    componentDidMount(){
        let combo=window.location.pathname.split('/');
        this.pk=combo[2]
        fetch("http://127.0.0.1:8000/rent/"+this.pk + "/")
            .then (res => res.json())
            .then(

                (result) =>{
                    this.setState({
                        isLoaded:true,
                        car: result,
                    });
                    // this.range=result;

                },
                (error) =>{
                    this.setState({
                        isLoaded:false,
                        error});
                }
            )

    }
    render() {
        const {error, isLoaded, car, models} = this.state;
        let combo=window.location.pathname.split('/');
        this.pk=combo[2]
        console.log(car.car)
        return (

            <div key={car.pk}>

                <Link to="/rent">Rent</Link> / <Link to={`/rent/${car.pk}`}>{car.car}</Link>

                <h1>{car.car}</h1>
                <div>Описание: {car.dicription}</div>




            </div>
        );
    }
}

export default Car;