import React, {Component} from 'react';
import {Link} from "react-router-dom";
//import './newStyle.css'

class Cars extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        }

    }
    componentDidMount(){
        fetch("http://127.0.0.1:8000/cars/")
            .then (res => res.json())
            .then(

                (result) =>{
                    this.setState({
                        isLoaded:true,
                        items: result,
                    });
                },
                (error) =>{
                    this.setState({
                        isLoaded:false,
                        error});
                }
            )
    }
    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <p>{error.message}</p>
        } else if (!isLoaded) {
            return <p>LOADING</p>
        } else {
            return (
                <div>
                    <Link to="/cars">Cars</Link>
                    <h1 className='hello'>Cars</h1>


                    {items.map(item=>(
                        <div className={"block-level"} key={item.pk}>
                            <div className={"drop-shadow"}>
                                <Link to={`/cars/${item.pk}`}>{item.avto}</Link>
                                <br/>{item.description}
                            </div>

                        </div>
                    ))}
                </div>


            );
        }
    }
}

export default Cars;