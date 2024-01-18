/* eslint-disable */
export default class Currency {
    constructor(code, name) {
        this.code = code;
        this.name = name
    }

    get code() {
        return this._code;
    }

    set code(new_code) {
        this._code = new_code;
    }

    get name() {
        return this._name;
    }
    set name(new_name) {
        this._name = new_name;
    }

    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }
}