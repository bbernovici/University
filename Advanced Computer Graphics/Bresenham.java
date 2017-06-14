import java.applet.Applet;
import java.awt.*;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseEvent;

/*
    BOGDAN BERNOVICI
    GROUP: 1232A
    FILS
 */


//Don't change the name of the class
public class Bresenham extends Applet implements MouseListener, MouseMotionListener {
    int cordX, cordY;
    int lastCordX, lastCordY;
    Graphics buffer;
    Image img;
    int ok = 0;
    int counter = 1;

    public void init() {
        img = createImage(200, 200);
        setBackground(Color.black);
        buffer = img.getGraphics();
    }

    public void start() {
        addMouseListener(this);
        addMouseMotionListener(this);
        setSize(200, 200);
    }

    public void paint(Graphics g) {
        if (ok == 1) {
            buffer.fillRect(cordX, cordY, 10, 10);
            buffer.drawRect(cordX, cordY, 10, 10);
            this.drawBresenhamLine(buffer, lastCordX, lastCordY, cordX, cordY);
            g.drawImage(img, 0, 0, this);
        } else {
            buffer.setColor(Color.blue);
            buffer.fillRect(4, 9, 1, 1);
            buffer.drawRect(4, 9, 1, 1);
            this.drawBresenhamLine(buffer, 0, 0, 19, 9);
            this.drawBresenhamLine(buffer, 19, 9, 0, 19);
        }
    }

    public void update(Graphics g) {
        paint(g);
    }

    @Override
    public void mouseClicked(MouseEvent mouse) {
        // TODO Auto-generated method stub
        if (ok == 1) {
            lastCordX = this.cordX;
            lastCordY = this.cordY;
        }
        else {
            ok = 1;
            lastCordX = mouse.getX();
            lastCordY = mouse.getY();
        }
        this.cordX = mouse.getX();
        this.cordY = mouse.getY();
        repaint();
    }

    @Override
    public void mouseEntered(MouseEvent arg0) {
        // TODO Auto-generated method stub
    }

    @Override
    public void mouseExited(MouseEvent arg0) {
        // TODO Auto-generated method stub
    }

    @Override
    public void mousePressed(MouseEvent arg0) {
        // TODO Auto-generated method stub
    }

    @Override
    public void mouseReleased(MouseEvent arg0) {
        // TODO Auto-generated method stub
    }

    private void drawBresenhamLine(Graphics g, int x1, int y1, int x2, int y2) {
        int width = x2 - x1;
        int height = y2 - y1;
        int dx1 = 0, dy1 = 0, dx2 = 0, dy2 = 0;

        if (width<0) {
            dx1 = -1;
        }
        else if (width>0) {
            dx1 = 1;
        }

        if (height<0) {
            dy1 = -1;
        }
        else if (height>0) {
            dy1 = 1;
        }

        if (width<0) {
            dx2 = -1;
        }
        else if (width>0) {
            dx2 = 1;
        }

        int big = Math.abs(width);
        int small = Math.abs(height);

        if (!(big>small)) {
            big = Math.abs(height);
            small = Math.abs(width);
            if (height<0) {
                dy2 = -1;
            }
            else if (height>0) {
                dy2 = 1;
            }
            dx2 = 0;
        }
        int num = big >> 1;
        for (int i = 0;i<=big;i++) {
            g.fillRect(x1,y1, 1,1);
            g.drawRect(x1,y1,1,1);
            num = num + small;
            if(!(num<big)) {
                num = num - big;
                x1 = x1 + dx1;
                y1 = y1 + dy1;
            }
            else {
                x1 = x1 + dx2;
                y1 = y1 + dy2;
            }
        }
    }

    // Prima incercare este algoritmul de mai jos dar cumva imi da OutOfMemory in JVM, functioneaza doar pentru primele 4-5 linii si nu respecta mereu cadranele

//    private void drawBresenhamLine(Graphics g, int x1, int y1, int x2, int y2) {
//        int delta = 0;
//        int dx = Math.abs(x2 - x1);
//        int dy = Math.abs(y2 - y1);
//
//        //
//        int dx2 = (dx << 1);
//        int dy2 = (dy << 1);
//
//        int altX, altY;
//
//        if (x1 < x2) {
//            altX = 1;
//        } else {
//            altX = -1;
//        }
//
//
//        if (y1 < y2) {
//            altY = 1;
//        } else {
//            altY = -1;
//        }
//
//        if (dy <= dx) {
//            while (true) {
//                g.fillRect(x1, y1, 1, 1);
//                g.drawRect(x1, y1, 1, 1);
//                if (x1 == x2) {
//                    break;
//                }
//                x1 = x1 + altX;
//                delta = delta + dy2;
//                if (delta > dx) {
//                    y1 = y1 + altY;
//                    delta = delta - dx2;
//                }
//            }
//        }
//        else {
//            while (true) {
//                g.fillRect(x1, y1, 1, 1);
//                g.drawRect(x1, y1, 1, 1);
//                if (y1 == y2) {
//                    break;
//                }
//                y1 = y1 + altY;
//                delta = delta + dx2;
//                if (delta > dy) {
//                    y1 = y1 + altY;
//                    delta = delta - dy2;
//                }
//            }
//        }
//
//
//    }

    @Override
    public void mouseDragged(MouseEvent mouse) {
        if (ok == 1) {
            lastCordX = this.cordX;
            lastCordY = this.cordY;
        }
        else {
            ok = 1;
            lastCordX = mouse.getX();
            lastCordY = mouse.getY();
        }
        this.cordX = mouse.getX();
        this.cordY = mouse.getY();
        repaint();
    }

    @Override
    public void mouseMoved(MouseEvent e) {

    }
}
