/* eslint-disable */
export default class Building {
    constructor(sqft) {
        if (this.constructor !== Building && !this.evacuationWarningMessage) {
            throw Error('Class extending Buiding must override evacuationWarnigMessage');
        }
        this._sqft = sqft;
    }

    get sqft() {
        return this._sqft;
    }

    set sqft(new_sqft) {
        this._sqft = new_sqft;
    }
}