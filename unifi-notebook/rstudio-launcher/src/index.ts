// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

import {
  ILayoutRestorer, 
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  ICommandPalette/*, IFrame, InstanceTracker*/
} from '@jupyterlab/apputils';

import {
    ServerConnection
} from '@jupyterlab/services';

import {
  ILauncher
} from '@jupyterlab/launcher';

import { IMainMenu } from '@jupyterlab/mainmenu';

import '../style/index.css';

const RSTUDIO_ICON_CLASS = 'jp-RStudioIcon';

/**
 * The command IDs used by the rstudio plugin.
 */
namespace CommandIDs {
  export const createNew = 'jlab-ide:rstudio-session-launch';
};

/**
 * The rsession handler extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyter.extension.rstudio-session-launch',
  autoStart: true,
  requires: [ICommandPalette, ILayoutRestorer],
  optional: [ILauncher, IMainMenu],
  activate: activate,
};

/**
 * Export the plugin as default.
 */
export default extension;

/**
 * Activate the rsession extension.
 */
function activate(app: JupyterFrontEnd, palette: ICommandPalette, restorer: ILayoutRestorer, launcher: ILauncher | null, menu: IMainMenu | null): void {
  const category = 'Other';
  const command = CommandIDs.createNew;
  const { commands } = app;

  commands.addCommand(command, {
    label: 'Rstudio',
    caption: 'Start a new Rstudio Session',
    iconClass: RSTUDIO_ICON_CLASS,
    execute: () => {
      // Start up the rserver
      // let settings = ServerConnection.makeSettings();
      // let req = {
      //   url: settings.baseUrl + 'rsessionproxy',
      //   method: 'POST',
      //   data: {}
      // };
      // ServerConnection.makeRequest(req, settings).then(resp => {
      //   console.log("Started RStudio... ", resp.data.url);
      //   window.open(resp.data.url, 'RStudio Session');
      // });
      let settings = ServerConnection.makeSettings();
      let url = settings.baseUrl + 'rstudio';
      console.log(url);
      window.open(url, 'RStudio Session');
    }
  });

  // Add a launcher item if the launcher is available.
  if (launcher) {
    launcher.add({
      command,
      category: category,
      rank: 1
    });
  }

  if (palette) {
    palette.addItem({
      command,
      args: { isPalette: true },
      category: category
    });
  }

  if (menu) {
    menu.fileMenu.newMenu.addGroup([{ command }], 30);
  }

}

