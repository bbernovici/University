import java.applet.Applet;
import java.awt.event.MouseListener;
import java.awt.Graphics;
import java.awt.event.MouseEvent;

/**
 * Bogdan Bernovici - 1232A
 */

//Don't change the name of the class
public class CohenSutherland extends Applet implements MouseListener {
    //viewing screen
    int xmin, xmax, ymin, ymax;
    int mx0, my0, mx1, my1, ok = 0;

    public void start() {
        addMouseListener(this);
        setSize(500,500);
    }
    @Override
    public void init() {
        xmin = 100;
        xmax = 300;
        ymin = 100;
        ymax = 300;
    }

    @Override
    public void paint(Graphics g) {
        g.drawRect(xmin, ymin, xmax - xmin, ymax - ymin);

        //TO DO:
        //Draw the fragment of the line that is inside the rectangle
        if(ok==2) {
            drawSutherland(g, mx0, my0, mx1, my1);
            ok=0;
        }
    }

    public void drawSutherland(Graphics g, int x0, int y0, int x1, int y1) {
        String firstPos = checkPosition(x0, y0);
        String secondPos = checkPosition(x1, y1);
        int x = 0, y = 0;


        //Check if both points are inside
        if (firstPos.equals("i") && secondPos.equals("i")) {
            g.drawLine(x0, y0, x1, y1);
        }

        //If first one is not inside, then process the point
        if (!firstPos.equals("i")) {
            if (firstPos.equals("t")) {
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0);
                y = ymax;
            } else if (firstPos.equals("b")) {
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0);
                y = ymin;
            } else if (firstPos.equals("r")) {
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0);
                x = xmax;
            } else if (firstPos.equals("l")) {
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0);
                x = xmin;
            }
            x0 = x;
            y0 = y;
        }

        //The same as above for the second one
        if (!secondPos.equals("i")) {
            if (secondPos.equals("t")) {
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0);
                y = ymax;
            } else if (secondPos.equals("b")) {
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0);
                y = ymin;
            } else if (secondPos.equals("r")) {
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0);
                x = xmax;
            } else if (secondPos.equals("l")) {
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0);
                x = xmin;
            }
            x1 = x;
            y1 = y;
        }

        //This checks if at least one is not inside, so it can draw the line after processing
        if (!(firstPos.equals("i") && secondPos.equals("i"))) {
            g.drawLine(x0, y0, x1, y1);
        }
    }

    public String checkPosition(int x, int y) {
        String pos = "i"; //let's init as being inside the square

        //First check for the x-coordinate
        if (x < this.xmin) {
            pos = "l"; //left
        } else if (x > this.xmax) {
            pos = "r"; //right
        }

        //Then conclude by checking the y-coordinate
        if (y < this.ymin) {
            pos = "b"; //bottom
        } else if (y > this.ymax) {
            pos = "t"; //top
        }

        return pos;
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        if(ok==0) {
            mx0 = e.getX();
            my0 = e.getY();
        } else if(ok==1) {
            mx1 = e.getX();
            my1 = e.getY();
        }
        ok++;
        repaint();
    }

    @Override
    public void mousePressed(MouseEvent e) {

    }

    @Override
    public void mouseReleased(MouseEvent e) {

    }

    @Override
    public void mouseEntered(MouseEvent e) {

    }

    @Override
    public void mouseExited(MouseEvent e) {

    }
}
