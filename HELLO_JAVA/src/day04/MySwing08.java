package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 281, 350);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblFirst = new JLabel("첫별수:");
		lblFirst.setBounds(36, 26, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝별수:");
		lblLast.setBounds(36, 59, 57, 15);
		contentPane.add(lblLast);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(146, 23, 57, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		tfLast = new JTextField();
		tfLast.setColumns(10);
		tfLast.setBounds(146, 56, 57, 21);
		contentPane.add(tfLast);
		
		JButton btn = new JButton("별출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(36, 84, 167, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(36, 116, 167, 173);
		contentPane.add(ta);
	}
	
	public String drawStar(int cnt) {
		String ret = "";
		for(int i=0;i<cnt;i++) {
			ret += "*";
		}
		
		ret += "\n";
		return ret;
	}
	
	public void myclick() {
		String a = tfFirst.getText();
		String b = tfLast.getText();
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		
		String txt = "";
		for(int i=aa;i<=bb;i++) {
			txt += drawStar(i);
		}
//		txt += drawStar(1);
//		txt += drawStar(2);
		ta.setText(txt);
		
	}
}



















