//
//  ViewController.swift
//  testSparkleRelease
//
//  Created by Alex Perathoner on 28/12/22.
//

import Cocoa
import Sparkle

class ViewController: NSViewController, SPUUpdaterDelegate {
    @IBOutlet weak var checkBetaUpdatesOutlet: NSButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    
    func allowedChannels(for updater: SPUUpdater) -> Set<String> {
        if(checkBetaUpdatesOutlet.state == .on) {
            return Set(["beta"])
        } else {
            return Set()
        }
    }


}

