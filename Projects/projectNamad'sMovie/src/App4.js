import React from "react";
import PropTypes from "prop-types";


function Movies({ id, year, title, summary }) {
    return <h4>{title}</h4>
}

Movies.prototype = {
    id: PropTypes.number.isRequired,
    year: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    summary: PropTypes.string.isRequired,
}

export default Movies;
