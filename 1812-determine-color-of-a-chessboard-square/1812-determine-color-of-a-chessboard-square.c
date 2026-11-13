bool squareIsWhite(char* coordinates) {
    return ((coordinates[0] - 'a') % 2) == ((coordinates[1] - '0') % 2);
}